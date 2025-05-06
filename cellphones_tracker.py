import requests
from bs4 import BeautifulSoup
import re
import csv
from urllib.parse import urljoin, urlparse

# --- Cấu hình Logging (hoặc print đơn giản) ---
def logger_info(msg): print(f"INFO: {msg}")
def logger_warning(msg): print(f"WARNING: {msg}")
def logger_error(msg): print(f"ERROR: {msg}")

# --- Các hàm tiện ích trích xuất nhỏ ---

def _extract_product_id(tag_with_href_or_data):
    if not tag_with_href_or_data:
        return "0"
    href = tag_with_href_or_data.get("href")
    product_id = "0"
    data_id_val = tag_with_href_or_data.get('data-product-id') or \
                  tag_with_href_or_data.get('data-id') or \
                  tag_with_href_or_data.get('data-item-id') or \
                  tag_with_href_or_data.get('data-sku')
    if data_id_val:
        if data_id_val.isdigit(): product_id = data_id_val
        else:
            id_match_in_data = re.search(r'(\d+)', data_id_val)
            if id_match_in_data: product_id = id_match_in_data.group(1)
        if product_id != "0": return product_id
    if href:
        match = re.search(
            r"(?:product_id(?:=|/)|item_id(?:=|/)|variant_id(?:=|/)|id(?:=|/)|(?:/p/|/dp/|spid=|item=|product-)|(?:sku(?:=|/)))(\d+)",
            href, re.IGNORECASE
        )
        if match: product_id = match.group(1)
        elif "javascript:void(0)" not in href and not href.startswith("#"):
            path_parts = [part for part in urlparse(href).path.split('/') if part]
            if path_parts and path_parts[-1].isdigit(): product_id = path_parts[-1]
            else:
                query_params = urlparse(href).query
                query_match = re.search(r"(?:id|p|productid|itemid)=(\d+)", query_params, re.IGNORECASE)
                if query_match: product_id = query_match.group(1)
    return product_id if product_id else "0"

def _extract_image_url(img_element, base_url_parsed):
    if not img_element: return "N/A"
    possible_attrs = ["data-src", "data-lazy-src", "data-original", "data-lazyload", "data-src-retina", "src"]
    image_src = None
    for attr in possible_attrs:
        image_src = img_element.get(attr)
        if image_src: break
    if image_src:
        image_src = image_src.strip()
        if not image_src: return "N/A"
        parsed_src = urlparse(image_src)
        if not parsed_src.scheme and not parsed_src.netloc:
            if base_url_parsed.scheme and base_url_parsed.netloc:
                return urljoin(f"{base_url_parsed.scheme}://{base_url_parsed.netloc}", image_src)
            else: return "N/A"
        elif image_src.startswith("//"):
             return f"{base_url_parsed.scheme}:{image_src}"
        return image_src
    return "N/A"

def _extract_price(price_element_container, class_regex_list=None):
    if not price_element_container: return "0"
    if class_regex_list is None:
        class_regex_list = [
            r"price", r"amount", r"sale-price", r"final-price", r"current-price",
            r"product__price", r"price__value", r"price-item", r"special-price",
            r"item-variant-price"
        ]
    price_text_raw = ""
    for class_regex in class_regex_list:
        price_element = price_element_container.find(
            ["span", "div", "p", "strong", "b", "ins"],
            class_=re.compile(class_regex, re.IGNORECASE)
        )
        if price_element:
            price_text_raw = price_element.get_text(separator=" ", strip=True)
            break
    if not price_text_raw and price_element_container.name in ["span", "div", "p", "strong"]:
        if not price_element_container.find(["div", "ul", "table"]): # Avoid grabbing price from complex inner structures
            container_text = price_element_container.get_text(separator=" ", strip=True)
            if any(char.isdigit() for char in container_text): # Basic check if text might contain a price
                price_text_raw = container_text

    if price_text_raw:
        price_text_raw = re.sub(r"(?i)(giá|price|sale|chỉ còn|từ|đặc biệt|km|Giá bán|Giá gốc|Giá chỉ):?", "", price_text_raw).strip()
        price_matches = re.findall(r'[\d.,]+', price_text_raw)
        if price_matches:
            target_price_str = price_matches[0] # Often the first number is the main price
            # Handle cases like "1.234.567" (Vietnamese) and "1,234.56" (US)
            cleaned_price = ""
            if '.' in target_price_str and ',' in target_price_str:
                if target_price_str.rfind('.') > target_price_str.rfind(','): # e.g., 1.234.567,89 -> 1234567.89
                    cleaned_price = target_price_str.replace('.', '').replace(',', '.')
                else: # e.g., 1,234,567.89 -> 1234567.89
                    cleaned_price = target_price_str.replace(',', '')
            elif '.' in target_price_str: # Potentially 123.456 or 123.45
                if target_price_str.count('.') > 1: # Likely 123.456.789
                     cleaned_price = target_price_str.replace('.', '')
                else: # Could be 123.45 (decimal) or 123.456 (thousands)
                    if len(target_price_str.split('.')[-1]) > 2 : # e.g. 123.456 (no decimal part or long decimal part treated as no decimal)
                         cleaned_price = target_price_str.replace('.', '')
                    else: # e.g. 123.45
                         cleaned_price = target_price_str
            elif ',' in target_price_str: # Potentially 123,456 or 123,45
                if target_price_str.count(',') > 1: # Likely 123,456,789
                     cleaned_price = target_price_str.replace(',', '')
                else: # Could be 123,45 (decimal) or 123,456 (thousands)
                    cleaned_price = target_price_str.replace(',', '.') # Assume comma is decimal if only one
            else:
                cleaned_price = target_price_str

            # Extract only the main numeric part before any decimal for integer price
            final_numeric_price = "".join(filter(str.isdigit, cleaned_price.split('.')[0]))
            if final_numeric_price: return final_numeric_price
    return "0"

def _normalize_name(name_element_or_string):
    if name_element_or_string is None: return "N/A"
    if hasattr(name_element_or_string, 'get_text'):
        text = name_element_or_string.get_text(separator=' ', strip=True)
    elif isinstance(name_element_or_string, str):
        text = name_element_or_string.strip()
    else:
        return "N/A"
    # Remove common prefixes/suffixes or normalize spacing
    text = re.sub(r'\s{2,}', ' ', text) # Replace multiple spaces with single
    text = re.sub(r'^(Xem chi tiết|Chi tiết sản phẩm)\s*:\s*', '', text, flags=re.IGNORECASE)
    return text if text else "N/A"

def _extract_base_product_name(name_str):
    if not name_str or name_str == "N/A":
        return "Sản phẩm không xác định"
    
    name_str = name_str.lower()
    # Common patterns to remove (capacities, colors, specific editions)
    # This list can be expanded based on observed product names
    patterns_to_remove = [
        r'\s*\d+gb', r'\s*\d+tb', r'\s*\d+g', r'\s*\d+t', # Capacities
        r'\s*\|\s*chính hãng.*', r'\s*\(chính hãng.*\)', # "Chính hãng" variants
        r'\s*\(vn/a\)', r'\s*vn/a', # VN/A
        r'\s*phiên bản.*', r'\s*bản.*', # Editions
        # Common color names (add more as needed)
        r'\s*-\s*(titan tự nhiên|titan trắng|titan xanh|titan đen|đen|trắng|xanh|vàng|hồng|đỏ|tím|bạc|xám|graphite|sierra blue|alpine green|pacific blue|gold|silver|space gray|midnight|starlight).*',
        r'\s*\((titan tự nhiên|titan trắng|titan xanh|titan đen|đen|trắng|xanh|vàng|hồng|đỏ|tím|bạc|xám|graphite|sierra blue|alpine green|pacific blue|gold|silver|space gray|midnight|starlight)\).*',
        r'\s*(titan tự nhiên|titan trắng|titan xanh|titan đen|đen|trắng|xanh|vàng|hồng|đỏ|tím|bạc|xám|graphite|sierra blue|alpine green|pacific blue|gold|silver|space gray|midnight|starlight)$'
    ]
    
    base_name = name_str
    for pattern in patterns_to_remove:
        base_name = re.sub(pattern, '', base_name, flags=re.IGNORECASE)
    
    # Remove trailing characters like '-' or extra spaces
    base_name = base_name.strip(' -')
    
    # Capitalize words for better display
    base_name = ' '.join(word.capitalize() for word in base_name.split())
    
    return base_name if base_name else "Sản phẩm không xác định"


def fetch_html_content(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Connection': 'keep-alive'
        }
        response = requests.get(url, headers=headers, timeout=20)
        response.raise_for_status()
        return response.text
    except requests.exceptions.Timeout:
        logger_error(f"Timeout khi lấy HTML từ {url}")
        return None
    except requests.exceptions.HTTPError as e:
        logger_error(f"Lỗi HTTP {e.response.status_code} khi lấy HTML từ {url}: {e}")
        return None
    except requests.exceptions.RequestException as e:
        logger_error(f"Lỗi chung khi lấy HTML từ {url}: {e}")
        return None

def _parse_method_1_variants(soup, base_url_parsed, source_url):
    products = []
    # More specific variant name classes, or broader ones if needed
    variant_name_classes = re.compile(r"item-variant-name|variant-name|product-option-name|option-label|name-version|label-option", re.IGNORECASE)
    variant_name_elements = soup.find_all(["strong", "span", "div", "label"], class_=variant_name_classes)
    
    # Also look for elements that might contain variant names by structure, e.g., inside specific list items or option selectors
    # This is highly site-dependent. Example: options in a select dropdown or radio buttons
    # variant_name_elements.extend(soup.select('ul.product-options > li > span.name')) # Example selector

    processed_parent_hashes = set()

    for variant_element in variant_name_elements:
        # Try to find a meaningful parent container for the variant
        parent_candidate = variant_element.find_parent(
            lambda tag: (tag.name == 'a' and tag.has_attr('href')) or \
                        (tag.name in ['div', 'li', 'article', 'label'] and \
                         tag.has_attr('class') and \
                         any(cls_keyword in " ".join(tag.get('class', [])) for cls_keyword in ["item", "product", "option", "variant", "box", "card", "tile", "choice"]))
        )
        container_to_search = parent_candidate if parent_candidate else variant_element.parent
        if not container_to_search: continue

        container_hash = hash(str(container_to_search)) # Simple way to avoid reprocessing very similar blocks
        if container_hash in processed_parent_hashes: continue
        processed_parent_hashes.add(container_hash)

        details = {"source_url": source_url, "variant_name": "N/A", "full_name": "N/A", "price": "0", "product_id": "0", "image_url": "N/A"}
        
        details["variant_name"] = _normalize_name(variant_element)
        
        link_for_id = container_to_search if container_to_search.name == 'a' else container_to_search.find("a", href=True)
        details["product_id"] = _extract_product_id(link_for_id or container_to_search)
        
        img_element = container_to_search.find("img")
        if img_element:
            details["image_url"] = _extract_image_url(img_element, base_url_parsed)
            alt_name = _normalize_name(img_element.get("alt"))
            if alt_name != "N/A" and details["full_name"] == "N/A": # Prioritize alt text for full name if available
                details["full_name"] = alt_name
        
        details["price"] = _extract_price(container_to_search)

        # Try to find a more general product name if full_name is still N/A
        if details["full_name"] == "N/A":
            # Look for a heading or prominent title element higher up or nearby
            product_title_el = container_to_search.find_previous(["h1", "h2", "h3"]) or \
                               soup.find(["h1", "h2"], class_=re.compile(r"product-title|page-title", re.IGNORECASE))
            if product_title_el:
                details["full_name"] = _normalize_name(product_title_el)
        
        if details["full_name"] == "N/A" and details["variant_name"] != "N/A":
            details["full_name"] = details["variant_name"] # Fallback if no better full_name found
        elif details["variant_name"] == "N/A" and details["full_name"] != "N/A" and details["full_name"] != details["image_url"]:
            # If variant_name is missing but full_name is good, this might be a single-variant product
            details["variant_name"] = details["full_name"]

        if details["product_id"] != "0" or details["price"] != "0" or details["image_url"] != "N/A" or (details["variant_name"] != "N/A" and details["variant_name"] != "Sản phẩm không xác định"):
            products.append(details)
            
    return products

def _parse_method_2_product_blocks(soup, base_url_parsed, source_url, processed_ids_from_method1):
    products = []
    product_block_regex = re.compile(
        r"product-item|product-card|product-block|product-box|product-info|item-cell|"
        r"product__item|product-container|product-wrapper|product-tile|product-listing-item|"
        r"variant-option|product[_-]loop|item-info|box-product|product-thumb|product-layout|"
        r"product[ _-]grid[ _-]item|product[ _-]list[ _-]item", # Added more general classes
        re.IGNORECASE
    )
    potential_product_blocks = soup.find_all(["div", "li", "a", "article", "section"], class_=product_block_regex)
    potential_product_blocks.extend(soup.find_all(attrs={"data-product-id": True}))
    potential_product_blocks.extend(soup.find_all(attrs={"data-sku": True}))
    # Add role attributes commonly used for products
    potential_product_blocks.extend(soup.find_all(attrs={"role": re.compile(r"listitem|product", re.IGNORECASE)}))


    existing_identifiers_method2 = set() 

    for block in potential_product_blocks:
        details = {"source_url": source_url, "variant_name": "N/A", "full_name": "N/A", "price": "0", "product_id": "0", "image_url": "N/A"}
        
        block_pid = block.get('data-product-id') or block.get('data-id') or block.get('data-sku')
        if block_pid and block_pid.isdigit(): details["product_id"] = block_pid
        else:
            href_source_tag = block if block.name == 'a' else block.find('a', href=True)
            details["product_id"] = _extract_product_id(href_source_tag or block)

        # Name extraction: prioritize specific classes, then general headings, then attributes
        name_el_candidates_classes = re.compile(r"product-name|product-title|title|name|heading|item-name|product__title|product-link__title", re.IGNORECASE)
        name_el = block.find(["h1", "h2", "h3", "h4", "h5", "p", "div", "span", "a"], class_=name_el_candidates_classes)
        
        if name_el:
            # If name_el is an 'a' tag, it might also be the href_source_tag. Avoid double duty if it's just a link.
            # We want the most descriptive name.
            temp_name = _normalize_name(name_el)
            # If the name is very short and the block is an 'a' tag, it might just be "View" or similar.
            # Prefer a more descriptive title from the block itself if available.
            if block.get('title') and (len(temp_name) < 10 or name_el.name == 'a'):
                 details["variant_name"] = _normalize_name(block.get('title'))
                 if details["full_name"] == "N/A": details["full_name"] = details["variant_name"]
            else:
                details["variant_name"] = temp_name
                if details["full_name"] == "N/A": details["full_name"] = temp_name

        elif block.get('aria-label'): # Check aria-label for accessibility names
            details["variant_name"] = _normalize_name(block.get('aria-label'))
            if details["full_name"] == "N/A": details["full_name"] = details["variant_name"]
        elif block.get('title'):
            details["variant_name"] = _normalize_name(block.get('title'))
            if details["full_name"] == "N/A": details["full_name"] = details["variant_name"]
        elif block.get('data-name'):
            details["variant_name"] = _normalize_name(block.get('data-name'))
            if details["full_name"] == "N/A": details["full_name"] = details["variant_name"]

        img_element = block.find("img")
        if img_element:
            details["image_url"] = _extract_image_url(img_element, base_url_parsed)
            alt_name = _normalize_name(img_element.get("alt"))
            if alt_name != "N/A" and alt_name != details["image_url"]:
                # If full_name is still N/A or less descriptive than alt_name, use alt_name
                if details["full_name"] == "N/A" or (details["full_name"] != "N/A" and len(alt_name) > len(details["full_name"]) and not details["full_name"].startswith(alt_name.split()[0])):
                     details["full_name"] = alt_name
                if details["variant_name"] == "N/A": # If variant name is also missing, alt can be a candidate
                     details["variant_name"] = alt_name


        if details["full_name"] == "N/A" and details["variant_name"] != "N/A":
            details["full_name"] = details["variant_name"]
        elif details["variant_name"] == "N/A" and details["full_name"] != "N/A":
            details["variant_name"] = details["full_name"]
            
        details["price"] = _extract_price(block)
        
        current_block_identifier = (details["product_id"], details["variant_name"], details["price"], details["image_url"])

        if details["product_id"] != "0" or details["price"] != "0" or details["image_url"] != "N/A" or (details["variant_name"] != "N/A" and details["variant_name"] != "Sản phẩm không xác định"):
            if current_block_identifier not in existing_identifiers_method2:
                # Check against method 1 only if the ID from method 2 is valid and was found by method 1
                if details["product_id"] != "0" and details["product_id"] in processed_ids_from_method1:
                    # This logic is to avoid adding a less complete version from method 2
                    # if method 1 already found a good entry for this product_id.
                    # However, direct comparison with m1_product was complex and removed for simplicity.
                    # The current approach relies on the local merge to handle duplicates.
                    # For now, if ID exists in method1, we might skip or refine later in merge.
                    # Let's assume for now that merging will handle it.
                    pass # Let merge handle potential duplicates/updates

                products.append(details)
                existing_identifiers_method2.add(current_block_identifier)
    return products


def _merge_products_locally(products_list, source_url):
    if not products_list: return []
    final_products_map = {}
    
    for p_idx, p in enumerate(products_list):
        pid, vname, fname, price, img_url = p["product_id"], p["variant_name"], p["full_name"], p["price"], p["image_url"]
        
        # Normalize names for key generation
        vname_key_part = (vname.lower().strip().replace(" ", "_") if vname and vname != "N/A" else "unknown_vname")
        fname_key_part = (fname.lower().strip().replace(" ", "_") if fname and fname != "N/A" else "unknown_fname")

        if pid != "0":
            # Prioritize ID, but also use variant name for distinct variants of same product ID if any
            product_key_tuple = (f"id_{pid}", f"vname_{vname_key_part}")
        else:
            # If no ID, use a combination of names, image, and price
            img_key_part = urlparse(img_url).path if img_url and img_url != "N/A" else "no_image"
            product_key_tuple = (f"fname_{fname_key_part}", f"vname_{vname_key_part}", f"img_{img_key_part}", f"price_{price}")

        # Handle completely generic entries by adding index to key
        if product_key_tuple == ("id_0", "vname_unknown_vname") or \
           product_key_tuple == ("fname_unknown_fname", "vname_unknown_vname", "no_image", f"price_{price}"):
             product_key_tuple = (product_key_tuple, p_idx)
        
        product_key = str(product_key_tuple) # Make key a string for dict

        if product_key not in final_products_map:
            final_products_map[product_key] = p.copy()
        else: # Update existing entry if new one has more/better info
            existing_p = final_products_map[product_key]
            if existing_p["product_id"] == "0" and p["product_id"] != "0": existing_p["product_id"] = p["product_id"]
            if (existing_p["price"] == "0" or existing_p["price"] == "N/A") and (p["price"] != "0" and p["price"] != "N/A"): existing_p["price"] = p["price"]
            if existing_p["image_url"] == "N/A" and p["image_url"] != "N/A": existing_p["image_url"] = p["image_url"]
            
            for name_field in ["variant_name", "full_name"]:
                current_val = existing_p.get(name_field, "N/A")
                new_val = p.get(name_field, "N/A")
                if (current_val == "N/A" or current_val == "Sản phẩm không xác định") and (new_val != "N/A" and new_val != "Sản phẩm không xác định"):
                    existing_p[name_field] = new_val
                elif (new_val != "N/A" and new_val != "Sản phẩm không xác định") and len(new_val) > len(current_val):
                    existing_p[name_field] = new_val
            existing_p["source_url"] = source_url # Ensure source_url is consistent or updated if needed
    return list(final_products_map.values())

def get_all_product_details_from_html(html_content, source_url="N/A"):
    if not html_content:
        logger_warning(f"Nội dung HTML trống cho URL: {source_url}")
        return []
    soup = BeautifulSoup(html_content, "html.parser")
    parsed_source_url = urlparse(source_url)
    all_products_on_page = []
    
    products_method1 = _parse_method_1_variants(soup, parsed_source_url, source_url)
    all_products_on_page.extend(products_method1)
    
    processed_ids_from_method1 = {p["product_id"] for p in products_method1 if p["product_id"] != "0"}
    
    products_method2 = _parse_method_2_product_blocks(soup, parsed_source_url, source_url, processed_ids_from_method1)
    all_products_on_page.extend(products_method2)
    
    merged_products = _merge_products_locally(all_products_on_page, source_url)
    
    # Post-merge cleanup and name inference
    for p in merged_products:
        if (p["full_name"] == "N/A" or p["full_name"] == "Sản phẩm không xác định") and (p["variant_name"] != "N/A" and p["variant_name"] != "Sản phẩm không xác định"):
            p["full_name"] = p["variant_name"]
        elif (p["variant_name"] == "N/A" or p["variant_name"] == "Sản phẩm không xác định") and \
             (p["full_name"] != "N/A" and p["full_name"] != "Sản phẩm không xác định") and \
             p["full_name"] != p["image_url"]: # Avoid using image URL as name
            p["variant_name"] = p["full_name"]

        # Try to infer name from image URL if other names are poor
        if (p["variant_name"] == "N/A" or p["variant_name"] == "Sản phẩm không xác định" or len(p["variant_name"]) < 5) and \
           p["image_url"] != "N/A" and not p["image_url"].startswith("data:"):
            try:
                img_path = urlparse(p["image_url"]).path
                img_filename = img_path.split('/')[-1]
                name_from_img = re.sub(r'\.(jpg|jpeg|png|gif|webp|svg|avif)$', '', img_filename, flags=re.IGNORECASE)
                name_from_img = name_from_img.replace('-', ' ').replace('_', ' ').strip()
                # Remove common image dimension patterns like -300x300
                name_from_img = re.sub(r'-\d+x\d+$', '', name_from_img)
                if name_from_img and len(name_from_img) > 3: # Basic check
                    p["variant_name"] = _normalize_name(name_from_img.capitalize())
                    if (p["full_name"] == "N/A" or p["full_name"] == "Sản phẩm không xác định"):
                        p["full_name"] = p["variant_name"]
            except Exception:
                pass # Ignore errors in name inference from image
    return merged_products

def generate_html_output(all_products_data, filename="scraped_products_interactive.html"):
    if not all_products_data:
        logger_info("Không có dữ liệu để xuất ra HTML.")
        return

    grouped_products = {}
    for product in all_products_data:
        base_name_key = _extract_base_product_name(product.get('full_name', 'N/A'))
        if not base_name_key or base_name_key == "N/A":
            base_name_key = 'Sản phẩm chưa được phân loại'
        
        if base_name_key not in grouped_products:
            grouped_products[base_name_key] = []
        grouped_products[base_name_key].append(product)

    html_content = f"""
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Danh sách Sản phẩm Trích xuất</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

            body {{
                font-family: 'Inter', sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f6f8; /* Light grayish blue background */
                color: #333;
                line-height: 1.6;
            }}
            .page-container {{
                width: 90%;
                max-width: 1600px; /* Wider for more content */
                margin: 30px auto;
                padding: 25px;
                background-color: #ffffff;
                border-radius: 16px; /* Softer corners */
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.07); /* More subtle shadow */
            }}
            header {{
                margin-bottom: 30px;
                padding-bottom: 20px;
                border-bottom: 1px solid #e0e0e0;
            }}
            h1 {{
                text-align: center;
                color: #2c3e50; 
                margin: 0 0 25px 0;
                font-weight: 700;
                font-size: 2.8em; /* Larger title */
            }}
            .search-filter-container {{
                display: flex;
                justify-content: center; /* Center the search bar */
                margin-bottom: 25px;
            }}
            #searchInput {{
                padding: 14px 20px;
                border: 1px solid #ced4da;
                border-radius: 8px;
                font-size: 1.05em;
                width: 100%;
                max-width: 600px; /* Wider search bar */
                box-sizing: border-box;
                transition: border-color 0.3s ease, box-shadow 0.3s ease;
                background-color: #fff;
            }}
            #searchInput:focus {{
                border-color: #007bff; /* Bootstrap primary blue */
                box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
                outline: none;
            }}
            .product-group {{
                margin-bottom: 35px;
                background-color: #ffffff;
                border-radius: 12px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.05);
                overflow: hidden;
                opacity: 0;
                transform: translateY(15px);
                animation: fadeInItem 0.4s ease-out forwards;
            }}
            .product-group.hidden {{ display: none !important; }}
            .product-group h2 {{
                font-size: 1.6em;
                color: #ffffff;
                background-color: #4a5568; /* Darker gray-blue for group headers */
                padding: 16px 22px;
                margin: 0;
                font-weight: 600; /* Slightly bolder */
                border-bottom: 1px solid #2d3748; /* Darker border */
                display: flex;
                justify-content: space-between;
                align-items: center;
            }}
            .product-group h2 .variant-count {{
                font-size: 0.75em;
                font-weight: 400;
                background-color: rgba(255,255,255,0.15);
                padding: 4px 10px;
                border-radius: 6px;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
            }}
            th, td {{
                padding: 15px 20px;
                text-align: left;
                vertical-align: middle;
                border-bottom: 1px solid #edf2f7; /* Lighter border for rows */
            }}
            th {{
                background-color: #f8f9fa; /* Very light gray for table headers */
                color: #495057; /* Darker gray text for headers
                font-weight: 600;
                font-size: 0.9em;
                text-transform: uppercase;
                letter-spacing: 0.05em;
            }}
            tr:last-child td {{
                border-bottom: none;
            }}
            tr:hover td {{
                background-color: #e9ecef; /* Subtle hover for rows */
            }}
            tr.hidden {{ display: none !important; }}
            td img {{
                max-width: 75px; /* Slightly smaller default image */
                max-height: 75px;
                display: block;
                margin: auto;
                border-radius: 6px;
                object-fit: contain;
                background-color: #fff;
                box-shadow: 0 1px 3px rgba(0,0,0,0.04);
                transition: transform 0.25s ease, box-shadow 0.25s ease;
            }}
            td img:hover {{
                transform: scale(1.15); /* Slightly larger zoom on hover */
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            }}
            .no-image {{
                color: #6c757d; /* Bootstrap muted text color */
                font-style: italic;
                text-align: center;
                display: flex;
                align-items: center;
                justify-content: center;
                height: 75px; width:75px;
                background-color:#e9ecef;
                margin:auto; border-radius: 6px;
                font-size: 0.8em;
            }}
            .url-cell {{ max-width: 180px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }}
            .url-cell a {{ color: #007bff; text-decoration: none; font-weight: 500; }}
            .url-cell a:hover {{ color: #0056b3; text-decoration: underline; }}
            .price-cell {{
                font-weight: 600;
                color: #28a745; /* Bootstrap success green for price */
                font-size: 1.05em;
                white-space: nowrap;
            }}
            .variant-name-cell, .full-name-cell {{ /* Added full-name-cell for consistency if used */
                font-weight: 500;
                color: #343a40; /* Darker text for names */
            }}
            .no-results {{
                text-align: center;
                padding: 40px 20px;
                font-size: 1.25em;
                color: #6c757d;
                display: none; /* Hidden by default */
                width: 100%;
                background-color: #fff;
                border-radius: 8px;
                margin-top: 20px;
            }}

            @keyframes fadeInItem {{
                from {{ opacity: 0; transform: translateY(15px); }}
                to {{ opacity: 1; transform: translateY(0); }}
            }}
        </style>
    </head>
    <body>
        <div class="page-container">
            <header>
                <h1>Danh sách Sản phẩm</h1>
                <div class="search-filter-container">
                    <input type="text" id="searchInput" onkeyup="filterProducts()" placeholder="Tìm kiếm sản phẩm (ví dụ: iPhone 15, Titan Xanh, 256GB)...">
                </div>
            </header>
<!-- Đặt đoạn này ví dụ sau thẻ </header> hoặc trước <div id="productListing"> -->
<div style="text-align: center; margin-bottom: 25px; padding: 15px; background-color: #eef2f7; border-radius: 8px; border: 1px solid #d1d9e6;">
    <p style="margin-bottom: 10px; font-size: 1.1em; color: #333; font-weight:500;"><strong>Quản lý Dữ liệu:</strong></p>
    <a 
       href="https://github.com/trung051/Toolchekgia/actions/workflows/update_product_data.yml" 
 
       target="_blank" 
       rel="noopener noreferrer"
       style="display: inline-block; padding: 12px 25px; background-color: #28a745; color: white; text-decoration: none; border-radius: 6px; font-size: 1em; font-weight: 500; box-shadow: 0 2px 5px rgba(0,0,0,0.15); transition: background-color 0.2s ease, transform 0.2s ease;"
       onmouseover="this.style.backgroundColor='#218838';"
       onmouseout="this.style.backgroundColor='#28a745';"
       onmousedown="this.style.transform='scale(0.98)';"
       onmouseup="this.style.transform='scale(1)';">
        🚀 Chạy Cập Nhật Dữ Liệu (Qua GitHub Actions)
    </a>
    <p style="font-size: 0.9em; color: #555; margin-top: 10px;">
        (Bạn sẽ được chuyển đến GitHub để kích hoạt quy trình cập nhật tự động. Sau khi chạy xong, hãy đợi vài phút rồi tải lại trang này.)
    </p>
</div>

            <div id="productListing">
    """

    sorted_group_names = sorted(grouped_products.keys(), key=lambda x: (x.isdigit(), x))
    animation_delay_step = 0.04 # Slightly faster animation stagger

    for idx, base_name_key in enumerate(sorted_group_names):
        products_in_group = grouped_products[base_name_key]
        
        # Sort variants within the group, e.g., by price or variant name
        products_in_group.sort(key=lambda p: (
            int(p.get('price', '0')) if p.get('price', '0').isdigit() else float('inf'),
            p.get('variant_name', '').lower()
        ))

        html_content += f"""
                <div class="product-group" style="animation-delay: {idx * animation_delay_step}s;">
                    <h2>{base_name_key} <span class="variant-count">{len(products_in_group)} máy</span></h2>
                    <table>
                        <thead>
                            <tr>
                                <th style="width: 4%;">STT</th>
                                <th style="width: 12%;">Nguồn</th>
                                <th style="width: 30%;">Tên máy (Variant)</th>
                                <th style="width: 30%;">Tên Đầy Đủ (Full Name)</th>
                                <th style="width: 12%;">Hình ảnh</th>
                                <th style="width: 12%;">Giá</th>
                            </tr>
                        </thead>
                        <tbody>
        """
        for i, product in enumerate(products_in_group):
            image_url_val = product.get('image_url', 'N/A')
            image_tag = '<div class="no-image"><span>Ảnh lỗi</span></div>'
            if image_url_val and image_url_val != 'N/A' and not image_url_val.startswith("data:"):
                image_tag = f'<img src="{image_url_val}" alt="{product.get("variant_name", "Hình ảnh sản phẩm")}" onError="this.style.display=\'none\'; this.nextElementSibling.style.display=\'flex\';">'
                image_tag += '<div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div>'
            elif image_url_val and image_url_val.startswith("data:"):
                image_tag = f'<img src="{image_url_val}" alt="{product.get("variant_name", "Hình ảnh sản phẩm")}">'
            else:
                image_tag = '<div class="no-image"><span>Không có ảnh</span></div>'

            source_url_display = product.get('source_url', 'N/A')
            if len(source_url_display) > 35: # Shorter display for URL
                source_url_display = source_url_display[:32] + "..."

            price_val = product.get('price', '0')
            price_display = "Liên hệ"
            if price_val != "0" and price_val != "N/A":
                try:
                    price_num = int(float(price_val)) # Ensure it's treated as float first for "123.0" cases
                    price_display = f"{price_num:,}".replace(",",".") + "&nbsp;₫"
                except ValueError:
                    price_display = price_val # Show original if not convertible
            
            variant_name_display = product.get('variant_name', 'N/A')
            full_name_display = product.get('full_name', 'N/A')

            html_content += f"""
                        <tr data-variant-name="{variant_name_display.lower()}" data-full-name="{full_name_display.lower()}">
                            <td>{i+1}</td>
                            <td class="url-cell"><a href="{product.get('source_url', '#')}" target="_blank" title="{product.get('source_url', '')}">{source_url_display}</a></td>
                            <td class="variant-name-cell">{variant_name_display}</td>
                            <td class="full-name-cell">{full_name_display}</td>
                            <td>{image_tag}</td>
                            <td class="price-cell">{price_display}</td>
                        </tr>
            """
        html_content += """
                        </tbody>
                    </table>
                </div>
        """

    html_content += """
            </div>
            <div class="no-results" id="noResultsMessage">Không tìm thấy sản phẩm nào phù hợp với tìm kiếm của bạn.</div>
        </div>

        <script>
            function filterProducts() {
                const searchInput = document.getElementById('searchInput');
                const searchValue = searchInput.value.toLowerCase().trim();
                const productGroups = document.querySelectorAll('#productListing .product-group');
                const noResultsMessage = document.getElementById('noResultsMessage');
                let anyGroupVisible = false;

                productGroups.forEach(group => {
                    const rows = group.querySelectorAll('tbody tr');
                    let visibleRowsInGroup = 0;
                    rows.forEach(row => {
                        const variantName = row.dataset.variantName || '';
                        const fullName = row.dataset.fullName || '';
                        
                        // Check if search value is part of variant name or full name
                        if (variantName.includes(searchValue) || fullName.includes(searchValue)) {
                            row.classList.remove('hidden');
                            visibleRowsInGroup++;
                        } else {
                            row.classList.add('hidden');
                        }
                    });

                    if (visibleRowsInGroup > 0) {
                        group.classList.remove('hidden');
                        anyGroupVisible = true;
                    } else {
                        group.classList.add('hidden');
                    }
                });

                if (!anyGroupVisible && searchValue !== "") { // Show message only if search term is entered
                    noResultsMessage.style.display = 'block';
                } else {
                    noResultsMessage.style.display = 'none';
                }
            }
            
            document.addEventListener('DOMContentLoaded', () => {
                const productGroups = document.querySelectorAll('#productListing .product-group');
                productGroups.forEach((group, index) => {
                    group.style.animationDelay = `${index * 0.04}s`;
                });
                // Initial filter call in case of page reload with search value (though less common for onkeyup)
                // filterProducts(); 
            });
        </script>
    </body>
    </html>
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_content)
        logger_info(f"Đã xuất dữ liệu HTML tương tác ra file: {filename}")
    except IOError as e:
        logger_error(f"Lỗi khi ghi file HTML tương tác {filename}: {e}")

# --- Các hàm xuất dữ liệu CSV và gộp dữ liệu toàn cục ---
def export_to_csv(all_products_data, filename="scraped_products.csv"):
    if not all_products_data:
        logger_info("Không có dữ liệu để xuất ra CSV.")
        return
    fieldnames = ["source_url", "variant_name", "full_name", "base_product_name", "image_url", "product_id", "price"]
    processed_data_for_csv = []
    for p_dict in all_products_data:
        row = {key: p_dict.get(key, "N/A" if key not in ["price", "product_id"] else "0") for key in fieldnames}
        if "base_product_name" not in p_dict: # Add base name if missing for CSV
             row["base_product_name"] = _extract_base_product_name(p_dict.get('full_name', 'N/A'))
        processed_data_for_csv.append(row)

    try:
        with open(filename, "w", newline="", encoding="utf-8-sig") as csvfile: # utf-8-sig for Excel compatibility
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(processed_data_for_csv)
        logger_info(f"Đã xuất dữ liệu ra file CSV: {filename}")
    except IOError as e:
        logger_error(f"Lỗi khi ghi file CSV {filename}: {e}")
    except Exception as e:
        logger_error(f"Một lỗi không xác định đã xảy ra khi ghi CSV: {e}")

def merge_all_data_globally(list_of_product_lists):
    master_product_map = {}
    for product_list_from_url in list_of_product_lists:
        for product in product_list_from_url:
            pid = product.get("product_id", "0")
            vname = product.get("variant_name", "N/A")
            img_url = product.get("image_url", "N/A")
            price = product.get("price", "0")
            fname = product.get("full_name", "N/A")
            
            # Normalize names for key generation
            vname_key_part = (vname.lower().strip().replace(" ", "_") if vname and vname != "N/A" else "unknown_vname")
            fname_key_part = (fname.lower().strip().replace(" ", "_") if fname and fname != "N/A" else "unknown_fname")

            if pid != "0":
                key_tuple = (f"id_{pid}", f"vname_{vname_key_part}")
            else:
                img_key_part = urlparse(img_url).path if img_url and img_url != "N/A" else "no_image"
                key_tuple = (f"fname_{fname_key_part}", f"vname_{vname_key_part}", f"img_{img_key_part}", f"price_{price}")
            
            # Make key a string
            key = str(key_tuple)

            if key not in master_product_map:
                master_product_map[key] = product.copy()
            else: # Update existing entry if new one has more/better info
                existing_p = master_product_map[key]
                if existing_p.get("product_id", "0") == "0" and pid != "0": existing_p["product_id"] = pid
                if (existing_p.get("price", "0") == "0" or existing_p.get("price", "0") == "N/A") and \
                   (price != "0" and price != "N/A"): existing_p["price"] = price
                if existing_p.get("image_url", "N/A") == "N/A" and img_url != "N/A": existing_p["image_url"] = img_url
                
                for name_field in ["variant_name", "full_name"]:
                    current_val = existing_p.get(name_field, "N/A")
                    new_val = product.get(name_field, "N/A")
                    if (current_val == "N/A" or current_val == "Sản phẩm không xác định") and \
                       (new_val != "N/A" and new_val != "Sản phẩm không xác định"):
                        existing_p[name_field] = new_val
                    elif (new_val != "N/A" and new_val != "Sản phẩm không xác định") and len(new_val) > len(current_val):
                        existing_p[name_field] = new_val
                # Could also merge source_urls if desired, e.g., into a list if product found on multiple sites
    return list(master_product_map.values())

# --- Cách sử dụng ---
if __name__ == "__main__":
    urls_to_scrape = [
        "https://cellphones.com.vn/iphone-15-pro-max.html",
        "https://cellphones.com.vn/iphone-15.html",
        "https://cellphones.com.vn/samsung-galaxy-s24-ultra.html",
        "https://cellphones.com.vn/xiaomi-14.html",
        "" # Added another category
        "https://cellphones.com.vn/dien-thoai-meizu-mblu-21.html",
        # "https://fptshop.com.vn/dien-thoai/samsung-galaxy-s23-fe",
    ]

    if not urls_to_scrape or ("URL_TRANG_1_CUA_BAN" in urls_to_scrape[0] and len(urls_to_scrape)==1) :
        logger_warning("Vui lòng cập nhật danh sách 'urls_to_scrape' bằng các URL thực tế của bạn.")
    else:
        all_extracted_data_from_all_urls = []
        for url_idx, url in enumerate(urls_to_scrape):
            logger_info(f"\n--- Đang xử lý URL {url_idx+1}/{len(urls_to_scrape)}: {url} ---")
            html_content = fetch_html_content(url)
            if html_content:
                logger_info(f"Đã lấy HTML thành công từ {url}. Đang trích xuất sản phẩm/biến thể...")
                products_on_this_page = get_all_product_details_from_html(html_content, source_url=url)
                if products_on_this_page:
                    logger_info(f"Tìm thấy {len(products_on_this_page)} sản phẩm/biến thể trên trang '{url}'.")
                    all_extracted_data_from_all_urls.append(products_on_this_page)
                else:
                    logger_warning(f"Không tìm thấy sản phẩm/biến thể nào trên trang '{url}' với các selector hiện tại.")
            else:
                logger_error(f"Không thể lấy nội dung HTML từ {url} hoặc nội dung trống.")

        if all_extracted_data_from_all_urls:
            logger_info(f"\n--- Hoàn tất trích xuất từ tất cả các URL. Tổng số danh sách sản phẩm (theo URL): {len(all_extracted_data_from_all_urls)} ---")
            final_master_list_of_products = merge_all_data_globally(all_extracted_data_from_all_urls)
            logger_info(f"Tổng cộng trích xuất và hợp nhất được {len(final_master_list_of_products)} sản phẩm/biến thể duy nhất từ tất cả các URL.")

            # Xuất ra file HTML tương tác mới
            generate_html_output(final_master_list_of_products, filename="tat_ca_san_pham_TUONG_TAC.html")

            # Xuất ra file CSV (Excel có thể mở được)
            export_to_csv(final_master_list_of_products, filename="tat_ca_san_pham_da_quet.csv")
        else:
            logger_info("\nKhông trích xuất được dữ liệu nào từ tất cả các URL đã cung cấp.")

    logger_info("\n--- Chương trình kết thúc ---")

