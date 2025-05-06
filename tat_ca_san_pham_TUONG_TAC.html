
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Danh sách Sản phẩm Trích xuất</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

            body {
                font-family: 'Inter', sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f6f8; /* Light grayish blue background */
                color: #333;
                line-height: 1.6;
            }
            .page-container {
                width: 90%;
                max-width: 1600px; /* Wider for more content */
                margin: 30px auto;
                padding: 25px;
                background-color: #ffffff;
                border-radius: 16px; /* Softer corners */
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.07); /* More subtle shadow */
            }
            header {
                margin-bottom: 30px;
                padding-bottom: 20px;
                border-bottom: 1px solid #e0e0e0;
            }
            h1 {
                text-align: center;
                color: #2c3e50; 
                margin: 0 0 25px 0;
                font-weight: 700;
                font-size: 2.8em; /* Larger title */
            }
            .search-filter-container {
                display: flex;
                justify-content: center; /* Center the search bar */
                margin-bottom: 25px;
            }
            #searchInput {
                padding: 14px 20px;
                border: 1px solid #ced4da;
                border-radius: 8px;
                font-size: 1.05em;
                width: 100%;
                max-width: 600px; /* Wider search bar */
                box-sizing: border-box;
                transition: border-color 0.3s ease, box-shadow 0.3s ease;
                background-color: #fff;
            }
            #searchInput:focus {
                border-color: #007bff; /* Bootstrap primary blue */
                box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
                outline: none;
            }
            .product-group {
                margin-bottom: 35px;
                background-color: #ffffff;
                border-radius: 12px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.05);
                overflow: hidden;
                opacity: 0;
                transform: translateY(15px);
                animation: fadeInItem 0.4s ease-out forwards;
            }
            .product-group.hidden { display: none !important; }
            .product-group h2 {
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
            }
            .product-group h2 .variant-count {
                font-size: 0.75em;
                font-weight: 400;
                background-color: rgba(255,255,255,0.15);
                padding: 4px 10px;
                border-radius: 6px;
            }
            table {
                width: 100%;
                border-collapse: collapse;
            }
            th, td {
                padding: 15px 20px;
                text-align: left;
                vertical-align: middle;
                border-bottom: 1px solid #edf2f7; /* Lighter border for rows */
            }
            th {
                background-color: #f8f9fa; /* Very light gray for table headers */
                color: #495057; /* Darker gray text for headers
                font-weight: 600;
                font-size: 0.9em;
                text-transform: uppercase;
                letter-spacing: 0.05em;
            }
            tr:last-child td {
                border-bottom: none;
            }
            tr:hover td {
                background-color: #e9ecef; /* Subtle hover for rows */
            }
            tr.hidden { display: none !important; }
            td img {
                max-width: 75px; /* Slightly smaller default image */
                max-height: 75px;
                display: block;
                margin: auto;
                border-radius: 6px;
                object-fit: contain;
                background-color: #fff;
                box-shadow: 0 1px 3px rgba(0,0,0,0.04);
                transition: transform 0.25s ease, box-shadow 0.25s ease;
            }
            td img:hover {
                transform: scale(1.15); /* Slightly larger zoom on hover */
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            }
            .no-image {
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
            }
            .url-cell { max-width: 180px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
            .url-cell a { color: #007bff; text-decoration: none; font-weight: 500; }
            .url-cell a:hover { color: #0056b3; text-decoration: underline; }
            .price-cell {
                font-weight: 600;
                color: #28a745; /* Bootstrap success green for price */
                font-size: 1.05em;
                white-space: nowrap;
            }
            .variant-name-cell, .full-name-cell { /* Added full-name-cell for consistency if used */
                font-weight: 500;
                color: #343a40; /* Darker text for names */
            }
            .no-results {
                text-align: center;
                padding: 40px 20px;
                font-size: 1.25em;
                color: #6c757d;
                display: none; /* Hidden by default */
                width: 100%;
                background-color: #fff;
                border-radius: 8px;
                margin-top: 20px;
            }

            @keyframes fadeInItem {
                from { opacity: 0; transform: translateY(15px); }
                to { opacity: 1; transform: translateY(0); }
            }
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
       href="https://trung051.github.io/Toolchekgia/actions/workflows/update_product_data.yml" 
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
    
                <div class="product-group" style="animation-delay: 0.0s;">
                    <h2>Chọn Màu Để Xem Giá Và Chi Nhánh Có Hàng <span class="variant-count">3 máy</span></h2>
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
        
                        <tr data-variant-name="chọn màu để xem giá và chi nhánh có hàng" data-full-name="chọn màu để xem giá và chi nhánh có hàng">
                            <td>1</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/iphone-15.html" target="_blank" title="https://cellphones.com.vn/iphone-15.html">https://cellphones.com.vn/iphone...</a></td>
                            <td class="variant-name-cell">Chọn màu để xem giá và chi nhánh có hàng</td>
                            <td class="full-name-cell">Chọn màu để xem giá và chi nhánh có hàng</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-15-128-gbden.png" alt="Chọn màu để xem giá và chi nhánh có hàng" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">15.890.000&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="chọn màu để xem giá và chi nhánh có hàng" data-full-name="chọn màu để xem giá và chi nhánh có hàng">
                            <td>2</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/xiaomi-14.html" target="_blank" title="https://cellphones.com.vn/xiaomi-14.html">https://cellphones.com.vn/xiaomi...</a></td>
                            <td class="variant-name-cell">Chọn màu để xem giá và chi nhánh có hàng</td>
                            <td class="full-name-cell">Chọn màu để xem giá và chi nhánh có hàng</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/x/i/xiaomi-14-pre-xanh-la_1.png" alt="Chọn màu để xem giá và chi nhánh có hàng" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">18.990.000&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="chọn màu để xem giá và chi nhánh có hàng" data-full-name="chọn màu để xem giá và chi nhánh có hàng">
                            <td>3</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/samsung-galaxy-s24-ultra.html" target="_blank" title="https://cellphones.com.vn/samsung-galaxy-s24-ultra.html">https://cellphones.com.vn/samsun...</a></td>
                            <td class="variant-name-cell">Chọn màu để xem giá và chi nhánh có hàng</td>
                            <td class="full-name-cell">Chọn màu để xem giá và chi nhánh có hàng</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/g/a/galaxy-s24-ultra-vang_1_3.png" alt="Chọn màu để xem giá và chi nhánh có hàng" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">24.390.000&nbsp;₫</td>
                        </tr>
            
                        </tbody>
                    </table>
                </div>
        
                <div class="product-group" style="animation-delay: 0.04s;">
                    <h2>Iphone 15 <span class="variant-count">10 máy</span></h2>
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
        
                        <tr data-variant-name="iphone 15 128gb vang" data-full-name="iphone 15 128gb | chính hãng vn/a-vàng">
                            <td>1</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/iphone-15.html" target="_blank" title="https://cellphones.com.vn/iphone-15.html">https://cellphones.com.vn/iphone...</a></td>
                            <td class="variant-name-cell">Iphone 15 128gb vang</td>
                            <td class="full-name-cell">iPhone 15 128GB | Chính hãng VN/A-Vàng</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-15-128gb-vang.png" alt="Iphone 15 128gb vang" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">15.790.000&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="iphone 15 128gb | chính hãng vn/a-vàng" data-full-name="iphone 15 128gb | chính hãng vn/a-vàng">
                            <td>2</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/iphone-15.html" target="_blank" title="https://cellphones.com.vn/iphone-15.html">https://cellphones.com.vn/iphone...</a></td>
                            <td class="variant-name-cell">iPhone 15 128GB | Chính hãng VN/A-Vàng</td>
                            <td class="full-name-cell">iPhone 15 128GB | Chính hãng VN/A-Vàng</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-15-128gb-vang.png" alt="iPhone 15 128GB | Chính hãng VN/A-Vàng" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">15.790.000&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="iphone 15 128 gbden" data-full-name="iphone 15 128gb | chính hãng vn/a-đen">
                            <td>3</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/iphone-15.html" target="_blank" title="https://cellphones.com.vn/iphone-15.html">https://cellphones.com.vn/iphone...</a></td>
                            <td class="variant-name-cell">Iphone 15 128 gbden</td>
                            <td class="full-name-cell">iPhone 15 128GB | Chính hãng VN/A-Đen</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-15-128-gbden.png" alt="Iphone 15 128 gbden" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">15.890.000&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="iphone 15 128gb | chính hãng vn/a-hồng" data-full-name="iphone 15 128gb | chính hãng vn/a-hồng">
                            <td>4</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/iphone-15.html" target="_blank" title="https://cellphones.com.vn/iphone-15.html">https://cellphones.com.vn/iphone...</a></td>
                            <td class="variant-name-cell">iPhone 15 128GB | Chính hãng VN/A-Hồng</td>
                            <td class="full-name-cell">iPhone 15 128GB | Chính hãng VN/A-Hồng</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-15-hong.png" alt="iPhone 15 128GB | Chính hãng VN/A-Hồng" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">15.890.000&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="iphone 15 128gb | chính hãng vn/a-xanh dương" data-full-name="iphone 15 128gb | chính hãng vn/a-xanh dương">
                            <td>5</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/iphone-15.html" target="_blank" title="https://cellphones.com.vn/iphone-15.html">https://cellphones.com.vn/iphone...</a></td>
                            <td class="variant-name-cell">iPhone 15 128GB | Chính hãng VN/A-Xanh dương</td>
                            <td class="full-name-cell">iPhone 15 128GB | Chính hãng VN/A-Xanh dương</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-15-128gb-xanh-duong.png" alt="iPhone 15 128GB | Chính hãng VN/A-Xanh dương" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">15.890.000&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="iphone 15 128gb | chính hãng vn/a-xanh lá" data-full-name="iphone 15 128gb | chính hãng vn/a-xanh lá">
                            <td>6</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/iphone-15.html" target="_blank" title="https://cellphones.com.vn/iphone-15.html">https://cellphones.com.vn/iphone...</a></td>
                            <td class="variant-name-cell">iPhone 15 128GB | Chính hãng VN/A-Xanh lá</td>
                            <td class="full-name-cell">iPhone 15 128GB | Chính hãng VN/A-Xanh lá</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-15-128gb-xanh-la.png" alt="iPhone 15 128GB | Chính hãng VN/A-Xanh lá" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">15.890.000&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="iphone 15 128gb | chính hãng vn/a-đen" data-full-name="iphone 15 128gb | chính hãng vn/a-đen">
                            <td>7</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/iphone-15.html" target="_blank" title="https://cellphones.com.vn/iphone-15.html">https://cellphones.com.vn/iphone...</a></td>
                            <td class="variant-name-cell">iPhone 15 128GB | Chính hãng VN/A-Đen</td>
                            <td class="full-name-cell">iPhone 15 128GB | Chính hãng VN/A-Đen</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-15-128-gbden.png" alt="iPhone 15 128GB | Chính hãng VN/A-Đen" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">15.890.000&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="iphone 15 hong" data-full-name="iphone 15 128gb | chính hãng vn/a-hồng">
                            <td>8</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/iphone-15.html" target="_blank" title="https://cellphones.com.vn/iphone-15.html">https://cellphones.com.vn/iphone...</a></td>
                            <td class="variant-name-cell">Iphone 15 hong</td>
                            <td class="full-name-cell">iPhone 15 128GB | Chính hãng VN/A-Hồng</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-15-hong.png" alt="Iphone 15 hong" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">15.890.000&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="xanh dương" data-full-name="iphone 15 128gb | chính hãng vn/a-xanh dương">
                            <td>9</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/iphone-15.html" target="_blank" title="https://cellphones.com.vn/iphone-15.html">https://cellphones.com.vn/iphone...</a></td>
                            <td class="variant-name-cell">Xanh dương</td>
                            <td class="full-name-cell">iPhone 15 128GB | Chính hãng VN/A-Xanh dương</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-15-128gb-xanh-duong.png" alt="Xanh dương" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">15.890.000&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="xanh lá" data-full-name="iphone 15 128gb | chính hãng vn/a-xanh lá">
                            <td>10</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/iphone-15.html" target="_blank" title="https://cellphones.com.vn/iphone-15.html">https://cellphones.com.vn/iphone...</a></td>
                            <td class="variant-name-cell">Xanh lá</td>
                            <td class="full-name-cell">iPhone 15 128GB | Chính hãng VN/A-Xanh lá</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-15-128gb-xanh-la.png" alt="Xanh lá" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">15.890.000&nbsp;₫</td>
                        </tr>
            
                        </tbody>
                    </table>
                </div>
        
                <div class="product-group" style="animation-delay: 0.08s;">
                    <h2>Iphone 15 Pro Max <span class="variant-count">9 máy</span></h2>
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
        
                        <tr data-variant-name="chọn màu để xem giá và chi nhánh có hàng" data-full-name="iphone 15 pro max 256gb | chính hãng vn/a-titan đen">
                            <td>1</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/iphone-15-pro-max.html" target="_blank" title="https://cellphones.com.vn/iphone-15-pro-max.html">https://cellphones.com.vn/iphone...</a></td>
                            <td class="variant-name-cell">Chọn màu để xem giá và chi nhánh có hàng</td>
                            <td class="full-name-cell">iPhone 15 Pro Max 256GB | Chính hãng VN/A-Titan Đen</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone15-pro-max-titan-den.jpg" alt="Chọn màu để xem giá và chi nhánh có hàng" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">27.990.000&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="iphone 15 pro max 256gb | chính hãng vn/a-titan trắng" data-full-name="iphone 15 pro max 256gb | chính hãng vn/a-titan trắng">
                            <td>2</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/iphone-15-pro-max.html" target="_blank" title="https://cellphones.com.vn/iphone-15-pro-max.html">https://cellphones.com.vn/iphone...</a></td>
                            <td class="variant-name-cell">iPhone 15 Pro Max 256GB | Chính hãng VN/A-Titan Trắng</td>
                            <td class="full-name-cell">iPhone 15 Pro Max 256GB | Chính hãng VN/A-Titan Trắng</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone15-pro-max-titan-trang.jpg" alt="iPhone 15 Pro Max 256GB | Chính hãng VN/A-Titan Trắng" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">27.990.000&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="iphone 15 pro max 256gb | chính hãng vn/a-titan tự nhiên" data-full-name="iphone 15 pro max 256gb | chính hãng vn/a-titan tự nhiên">
                            <td>3</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/iphone-15-pro-max.html" target="_blank" title="https://cellphones.com.vn/iphone-15-pro-max.html">https://cellphones.com.vn/iphone...</a></td>
                            <td class="variant-name-cell">iPhone 15 Pro Max 256GB | Chính hãng VN/A-Titan Tự Nhiên</td>
                            <td class="full-name-cell">iPhone 15 Pro Max 256GB | Chính hãng VN/A-Titan Tự Nhiên</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone15-pro-max-titan-nau.jpg" alt="iPhone 15 Pro Max 256GB | Chính hãng VN/A-Titan Tự Nhiên" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">27.990.000&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="iphone 15 pro max 256gb | chính hãng vn/a-titan xanh" data-full-name="iphone 15 pro max 256gb | chính hãng vn/a-titan xanh">
                            <td>4</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/iphone-15-pro-max.html" target="_blank" title="https://cellphones.com.vn/iphone-15-pro-max.html">https://cellphones.com.vn/iphone...</a></td>
                            <td class="variant-name-cell">iPhone 15 Pro Max 256GB | Chính hãng VN/A-Titan Xanh</td>
                            <td class="full-name-cell">iPhone 15 Pro Max 256GB | Chính hãng VN/A-Titan Xanh</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone15-pro-max-titan-xanh.jpg" alt="iPhone 15 Pro Max 256GB | Chính hãng VN/A-Titan Xanh" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">27.990.000&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="iphone 15 pro max 256gb | chính hãng vn/a-titan đen" data-full-name="iphone 15 pro max 256gb | chính hãng vn/a-titan đen">
                            <td>5</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/iphone-15-pro-max.html" target="_blank" title="https://cellphones.com.vn/iphone-15-pro-max.html">https://cellphones.com.vn/iphone...</a></td>
                            <td class="variant-name-cell">iPhone 15 Pro Max 256GB | Chính hãng VN/A-Titan Đen</td>
                            <td class="full-name-cell">iPhone 15 Pro Max 256GB | Chính hãng VN/A-Titan Đen</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone15-pro-max-titan-den.jpg" alt="iPhone 15 Pro Max 256GB | Chính hãng VN/A-Titan Đen" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">27.990.000&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="titan trắng" data-full-name="iphone 15 pro max 256gb | chính hãng vn/a-titan trắng">
                            <td>6</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/iphone-15-pro-max.html" target="_blank" title="https://cellphones.com.vn/iphone-15-pro-max.html">https://cellphones.com.vn/iphone...</a></td>
                            <td class="variant-name-cell">Titan Trắng</td>
                            <td class="full-name-cell">iPhone 15 Pro Max 256GB | Chính hãng VN/A-Titan Trắng</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone15-pro-max-titan-trang.jpg" alt="Titan Trắng" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">27.990.000&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="titan tự nhiên" data-full-name="iphone 15 pro max 256gb | chính hãng vn/a-titan tự nhiên">
                            <td>7</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/iphone-15-pro-max.html" target="_blank" title="https://cellphones.com.vn/iphone-15-pro-max.html">https://cellphones.com.vn/iphone...</a></td>
                            <td class="variant-name-cell">Titan Tự Nhiên</td>
                            <td class="full-name-cell">iPhone 15 Pro Max 256GB | Chính hãng VN/A-Titan Tự Nhiên</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone15-pro-max-titan-nau.jpg" alt="Titan Tự Nhiên" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">27.990.000&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="titan xanh" data-full-name="iphone 15 pro max 256gb | chính hãng vn/a-titan xanh">
                            <td>8</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/iphone-15-pro-max.html" target="_blank" title="https://cellphones.com.vn/iphone-15-pro-max.html">https://cellphones.com.vn/iphone...</a></td>
                            <td class="variant-name-cell">Titan Xanh</td>
                            <td class="full-name-cell">iPhone 15 Pro Max 256GB | Chính hãng VN/A-Titan Xanh</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone15-pro-max-titan-xanh.jpg" alt="Titan Xanh" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">27.990.000&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="titan đen" data-full-name="iphone 15 pro max 256gb | chính hãng vn/a-titan đen">
                            <td>9</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/iphone-15-pro-max.html" target="_blank" title="https://cellphones.com.vn/iphone-15-pro-max.html">https://cellphones.com.vn/iphone...</a></td>
                            <td class="variant-name-cell">Titan Đen</td>
                            <td class="full-name-cell">iPhone 15 Pro Max 256GB | Chính hãng VN/A-Titan Đen</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone15-pro-max-titan-den.jpg" alt="Titan Đen" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">27.990.000&nbsp;₫</td>
                        </tr>
            
                        </tbody>
                    </table>
                </div>
        
                <div class="product-group" style="animation-delay: 0.12s;">
                    <h2>Samsung Galaxy S24 Ultra <span class="variant-count">8 máy</span></h2>
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
        
                        <tr data-variant-name="galaxy s24 ultra den 1 1 3" data-full-name="samsung galaxy s24 ultra 12gb 256gb-đen">
                            <td>1</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/samsung-galaxy-s24-ultra.html" target="_blank" title="https://cellphones.com.vn/samsung-galaxy-s24-ultra.html">https://cellphones.com.vn/samsun...</a></td>
                            <td class="variant-name-cell">Galaxy s24 ultra den 1 1 3</td>
                            <td class="full-name-cell">Samsung Galaxy S24 Ultra 12GB 256GB-Đen</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/g/a/galaxy-s24-ultra-den-1_1_3.png" alt="Galaxy s24 ultra den 1 1 3" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">24.390.000&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="galaxy s24 ultra tim 1 3" data-full-name="samsung galaxy s24 ultra 12gb 256gb-tím">
                            <td>2</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/samsung-galaxy-s24-ultra.html" target="_blank" title="https://cellphones.com.vn/samsung-galaxy-s24-ultra.html">https://cellphones.com.vn/samsun...</a></td>
                            <td class="variant-name-cell">Galaxy s24 ultra tim 1 3</td>
                            <td class="full-name-cell">Samsung Galaxy S24 Ultra 12GB 256GB-Tím</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/g/a/galaxy-s24-ultra-tim_1_3.png" alt="Galaxy s24 ultra tim 1 3" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">24.390.000&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="galaxy s24 ultra vang 1 3" data-full-name="samsung galaxy s24 ultra 12gb 256gb-vàng">
                            <td>3</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/samsung-galaxy-s24-ultra.html" target="_blank" title="https://cellphones.com.vn/samsung-galaxy-s24-ultra.html">https://cellphones.com.vn/samsun...</a></td>
                            <td class="variant-name-cell">Galaxy s24 ultra vang 1 3</td>
                            <td class="full-name-cell">Samsung Galaxy S24 Ultra 12GB 256GB-Vàng</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/g/a/galaxy-s24-ultra-vang_1_3.png" alt="Galaxy s24 ultra vang 1 3" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">24.390.000&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="galaxy s24 ultra xam 1 3" data-full-name="samsung galaxy s24 ultra 12gb 256gb-xám">
                            <td>4</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/samsung-galaxy-s24-ultra.html" target="_blank" title="https://cellphones.com.vn/samsung-galaxy-s24-ultra.html">https://cellphones.com.vn/samsun...</a></td>
                            <td class="variant-name-cell">Galaxy s24 ultra xam 1 3</td>
                            <td class="full-name-cell">Samsung Galaxy S24 Ultra 12GB 256GB-Xám</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/g/a/galaxy-s24-ultra-xam_1_3.png" alt="Galaxy s24 ultra xam 1 3" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">24.390.000&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="samsung galaxy s24 ultra 12gb 256gb-tím" data-full-name="samsung galaxy s24 ultra 12gb 256gb-tím">
                            <td>5</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/samsung-galaxy-s24-ultra.html" target="_blank" title="https://cellphones.com.vn/samsung-galaxy-s24-ultra.html">https://cellphones.com.vn/samsun...</a></td>
                            <td class="variant-name-cell">Samsung Galaxy S24 Ultra 12GB 256GB-Tím</td>
                            <td class="full-name-cell">Samsung Galaxy S24 Ultra 12GB 256GB-Tím</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/g/a/galaxy-s24-ultra-tim_1_3.png" alt="Samsung Galaxy S24 Ultra 12GB 256GB-Tím" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">24.390.000&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="samsung galaxy s24 ultra 12gb 256gb-vàng" data-full-name="samsung galaxy s24 ultra 12gb 256gb-vàng">
                            <td>6</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/samsung-galaxy-s24-ultra.html" target="_blank" title="https://cellphones.com.vn/samsung-galaxy-s24-ultra.html">https://cellphones.com.vn/samsun...</a></td>
                            <td class="variant-name-cell">Samsung Galaxy S24 Ultra 12GB 256GB-Vàng</td>
                            <td class="full-name-cell">Samsung Galaxy S24 Ultra 12GB 256GB-Vàng</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/g/a/galaxy-s24-ultra-vang_1_3.png" alt="Samsung Galaxy S24 Ultra 12GB 256GB-Vàng" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">24.390.000&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="samsung galaxy s24 ultra 12gb 256gb-xám" data-full-name="samsung galaxy s24 ultra 12gb 256gb-xám">
                            <td>7</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/samsung-galaxy-s24-ultra.html" target="_blank" title="https://cellphones.com.vn/samsung-galaxy-s24-ultra.html">https://cellphones.com.vn/samsun...</a></td>
                            <td class="variant-name-cell">Samsung Galaxy S24 Ultra 12GB 256GB-Xám</td>
                            <td class="full-name-cell">Samsung Galaxy S24 Ultra 12GB 256GB-Xám</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/g/a/galaxy-s24-ultra-xam_1_3.png" alt="Samsung Galaxy S24 Ultra 12GB 256GB-Xám" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">24.390.000&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="samsung galaxy s24 ultra 12gb 256gb-đen" data-full-name="samsung galaxy s24 ultra 12gb 256gb-đen">
                            <td>8</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/samsung-galaxy-s24-ultra.html" target="_blank" title="https://cellphones.com.vn/samsung-galaxy-s24-ultra.html">https://cellphones.com.vn/samsun...</a></td>
                            <td class="variant-name-cell">Samsung Galaxy S24 Ultra 12GB 256GB-Đen</td>
                            <td class="full-name-cell">Samsung Galaxy S24 Ultra 12GB 256GB-Đen</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/g/a/galaxy-s24-ultra-den-1_1_3.png" alt="Samsung Galaxy S24 Ultra 12GB 256GB-Đen" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">24.390.000&nbsp;₫</td>
                        </tr>
            
                        </tbody>
                    </table>
                </div>
        
                <div class="product-group" style="animation-delay: 0.16s;">
                    <h2>Sản Phẩm Gợi Ý <span class="variant-count">1 máy</span></h2>
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
        
                        <tr data-variant-name="sản phẩm gợi ý" data-full-name="sản phẩm gợi ý">
                            <td>1</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/iphone-15-pro-max.html" target="_blank" title="https://cellphones.com.vn/iphone-15-pro-max.html">https://cellphones.com.vn/iphone...</a></td>
                            <td class="variant-name-cell">Sản phẩm gợi ý</td>
                            <td class="full-name-cell">Sản phẩm gợi ý</td>
                            <td><div class="no-image"><span>Không có ảnh</span></div></td>
                            <td class="price-cell">Liên hệ</td>
                        </tr>
            
                        </tbody>
                    </table>
                </div>
        
                <div class="product-group" style="animation-delay: 0.2s;">
                    <h2>Sản phẩm không xác định <span class="variant-count">4 máy</span></h2>
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
        
                        <tr data-variant-name="n/a" data-full-name="n/a">
                            <td>1</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/xiaomi-14.html" target="_blank" title="https://cellphones.com.vn/xiaomi-14.html">https://cellphones.com.vn/xiaomi...</a></td>
                            <td class="variant-name-cell">N/A</td>
                            <td class="full-name-cell">N/A</td>
                            <td><div class="no-image"><span>Không có ảnh</span></div></td>
                            <td class="price-cell">14&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="n/a" data-full-name="n/a">
                            <td>2</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/iphone-15-pro-max.html" target="_blank" title="https://cellphones.com.vn/iphone-15-pro-max.html">https://cellphones.com.vn/iphone...</a></td>
                            <td class="variant-name-cell">N/A</td>
                            <td class="full-name-cell">N/A</td>
                            <td><div class="no-image"><span>Không có ảnh</span></div></td>
                            <td class="price-cell">15&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="n/a" data-full-name="n/a">
                            <td>3</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/dien-thoai-meizu-mblu-21.html" target="_blank" title="https://cellphones.com.vn/dien-thoai-meizu-mblu-21.html">https://cellphones.com.vn/dien-t...</a></td>
                            <td class="variant-name-cell">N/A</td>
                            <td class="full-name-cell">N/A</td>
                            <td><div class="no-image"><span>Không có ảnh</span></div></td>
                            <td class="price-cell">21&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="n/a" data-full-name="n/a">
                            <td>4</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/samsung-galaxy-s24-ultra.html" target="_blank" title="https://cellphones.com.vn/samsung-galaxy-s24-ultra.html">https://cellphones.com.vn/samsun...</a></td>
                            <td class="variant-name-cell">N/A</td>
                            <td class="full-name-cell">N/A</td>
                            <td><div class="no-image"><span>Không có ảnh</span></div></td>
                            <td class="price-cell">24&nbsp;₫</td>
                        </tr>
            
                        </tbody>
                    </table>
                </div>
        
                <div class="product-group" style="animation-delay: 0.24s;">
                    <h2>Xiaomi 14 <span class="variant-count">6 máy</span></h2>
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
        
                        <tr data-variant-name="trắng" data-full-name="xiaomi 14 12gb 256gb-trắng">
                            <td>1</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/xiaomi-14.html" target="_blank" title="https://cellphones.com.vn/xiaomi-14.html">https://cellphones.com.vn/xiaomi...</a></td>
                            <td class="variant-name-cell">Trắng</td>
                            <td class="full-name-cell">Xiaomi 14 12GB 256GB-Trắng</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/x/i/xiaomi-14-pre-trang_1.png" alt="Trắng" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">18.990.000&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="xiaomi 14 12gb 256gb-trắng" data-full-name="xiaomi 14 12gb 256gb-trắng">
                            <td>2</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/xiaomi-14.html" target="_blank" title="https://cellphones.com.vn/xiaomi-14.html">https://cellphones.com.vn/xiaomi...</a></td>
                            <td class="variant-name-cell">Xiaomi 14 12GB 256GB-Trắng</td>
                            <td class="full-name-cell">Xiaomi 14 12GB 256GB-Trắng</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/x/i/xiaomi-14-pre-trang_1.png" alt="Xiaomi 14 12GB 256GB-Trắng" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">18.990.000&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="xiaomi 14 12gb 256gb-xanh" data-full-name="xiaomi 14 12gb 256gb-xanh">
                            <td>3</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/xiaomi-14.html" target="_blank" title="https://cellphones.com.vn/xiaomi-14.html">https://cellphones.com.vn/xiaomi...</a></td>
                            <td class="variant-name-cell">Xiaomi 14 12GB 256GB-Xanh</td>
                            <td class="full-name-cell">Xiaomi 14 12GB 256GB-Xanh</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/x/i/xiaomi-14-pre-xanh-la_1.png" alt="Xiaomi 14 12GB 256GB-Xanh" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">18.990.000&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="xiaomi 14 12gb 256gb-đen" data-full-name="xiaomi 14 12gb 256gb-đen">
                            <td>4</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/xiaomi-14.html" target="_blank" title="https://cellphones.com.vn/xiaomi-14.html">https://cellphones.com.vn/xiaomi...</a></td>
                            <td class="variant-name-cell">Xiaomi 14 12GB 256GB-Đen</td>
                            <td class="full-name-cell">Xiaomi 14 12GB 256GB-Đen</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/x/i/xiaomi-14-pre-den_1.png" alt="Xiaomi 14 12GB 256GB-Đen" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">18.990.000&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="xiaomi 14 pre den 1" data-full-name="xiaomi 14 12gb 256gb-đen">
                            <td>5</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/xiaomi-14.html" target="_blank" title="https://cellphones.com.vn/xiaomi-14.html">https://cellphones.com.vn/xiaomi...</a></td>
                            <td class="variant-name-cell">Xiaomi 14 pre den 1</td>
                            <td class="full-name-cell">Xiaomi 14 12GB 256GB-Đen</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/x/i/xiaomi-14-pre-den_1.png" alt="Xiaomi 14 pre den 1" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">18.990.000&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="xiaomi 14 pre xanh la 1" data-full-name="xiaomi 14 12gb 256gb-xanh">
                            <td>6</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/xiaomi-14.html" target="_blank" title="https://cellphones.com.vn/xiaomi-14.html">https://cellphones.com.vn/xiaomi...</a></td>
                            <td class="variant-name-cell">Xiaomi 14 pre xanh la 1</td>
                            <td class="full-name-cell">Xiaomi 14 12GB 256GB-Xanh</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/x/i/xiaomi-14-pre-xanh-la_1.png" alt="Xiaomi 14 pre xanh la 1" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">18.990.000&nbsp;₫</td>
                        </tr>
            
                        </tbody>
                    </table>
                </div>
        
                <div class="product-group" style="animation-delay: 0.28s;">
                    <h2>Điện Thoại Meizu Mblu 21 <span class="variant-count">7 máy</span></h2>
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
        
                        <tr data-variant-name="chọn màu để xem giá và chi nhánh có hàng" data-full-name="điện thoại meizu mblu 21 4gb 64gb - trắng">
                            <td>1</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/dien-thoai-meizu-mblu-21.html" target="_blank" title="https://cellphones.com.vn/dien-thoai-meizu-mblu-21.html">https://cellphones.com.vn/dien-t...</a></td>
                            <td class="variant-name-cell">Chọn màu để xem giá và chi nhánh có hàng</td>
                            <td class="full-name-cell">Điện thoại Meizu Mblu 21 4GB 64GB - Trắng</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/d/i/dien-thoai-meizu-mblu-21-trang.jpg" alt="Chọn màu để xem giá và chi nhánh có hàng" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">1.990.000&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="dien thoai meizu mblu 21 denn" data-full-name="điện thoại meizu mblu 21 4gb 64gb - đen">
                            <td>2</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/dien-thoai-meizu-mblu-21.html" target="_blank" title="https://cellphones.com.vn/dien-thoai-meizu-mblu-21.html">https://cellphones.com.vn/dien-t...</a></td>
                            <td class="variant-name-cell">Dien thoai meizu mblu 21 denn</td>
                            <td class="full-name-cell">Điện thoại Meizu Mblu 21 4GB 64GB - Đen</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/d/i/dien-thoai-meizu-mblu-21-denn.jpg" alt="Dien thoai meizu mblu 21 denn" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">1.990.000&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="dien thoai meizu mblu 21 xanh" data-full-name="điện thoại meizu mblu 21 4gb 64gb - xanh">
                            <td>3</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/dien-thoai-meizu-mblu-21.html" target="_blank" title="https://cellphones.com.vn/dien-thoai-meizu-mblu-21.html">https://cellphones.com.vn/dien-t...</a></td>
                            <td class="variant-name-cell">Dien thoai meizu mblu 21 xanh</td>
                            <td class="full-name-cell">Điện thoại Meizu Mblu 21 4GB 64GB - Xanh</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/d/i/dien-thoai-meizu-mblu-21-xanh.jpg" alt="Dien thoai meizu mblu 21 xanh" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">1.990.000&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="trắng" data-full-name="điện thoại meizu mblu 21 4gb 64gb - trắng">
                            <td>4</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/dien-thoai-meizu-mblu-21.html" target="_blank" title="https://cellphones.com.vn/dien-thoai-meizu-mblu-21.html">https://cellphones.com.vn/dien-t...</a></td>
                            <td class="variant-name-cell">Trắng</td>
                            <td class="full-name-cell">Điện thoại Meizu Mblu 21 4GB 64GB - Trắng</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/d/i/dien-thoai-meizu-mblu-21-trang.jpg" alt="Trắng" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">1.990.000&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="điện thoại meizu mblu 21 4gb 64gb - trắng" data-full-name="điện thoại meizu mblu 21 4gb 64gb - trắng">
                            <td>5</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/dien-thoai-meizu-mblu-21.html" target="_blank" title="https://cellphones.com.vn/dien-thoai-meizu-mblu-21.html">https://cellphones.com.vn/dien-t...</a></td>
                            <td class="variant-name-cell">Điện thoại Meizu Mblu 21 4GB 64GB - Trắng</td>
                            <td class="full-name-cell">Điện thoại Meizu Mblu 21 4GB 64GB - Trắng</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/d/i/dien-thoai-meizu-mblu-21-trang.jpg" alt="Điện thoại Meizu Mblu 21 4GB 64GB - Trắng" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">1.990.000&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="điện thoại meizu mblu 21 4gb 64gb - xanh" data-full-name="điện thoại meizu mblu 21 4gb 64gb - xanh">
                            <td>6</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/dien-thoai-meizu-mblu-21.html" target="_blank" title="https://cellphones.com.vn/dien-thoai-meizu-mblu-21.html">https://cellphones.com.vn/dien-t...</a></td>
                            <td class="variant-name-cell">Điện thoại Meizu Mblu 21 4GB 64GB - Xanh</td>
                            <td class="full-name-cell">Điện thoại Meizu Mblu 21 4GB 64GB - Xanh</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/d/i/dien-thoai-meizu-mblu-21-xanh.jpg" alt="Điện thoại Meizu Mblu 21 4GB 64GB - Xanh" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">1.990.000&nbsp;₫</td>
                        </tr>
            
                        <tr data-variant-name="điện thoại meizu mblu 21 4gb 64gb - đen" data-full-name="điện thoại meizu mblu 21 4gb 64gb - đen">
                            <td>7</td>
                            <td class="url-cell"><a href="https://cellphones.com.vn/dien-thoai-meizu-mblu-21.html" target="_blank" title="https://cellphones.com.vn/dien-thoai-meizu-mblu-21.html">https://cellphones.com.vn/dien-t...</a></td>
                            <td class="variant-name-cell">Điện thoại Meizu Mblu 21 4GB 64GB - Đen</td>
                            <td class="full-name-cell">Điện thoại Meizu Mblu 21 4GB 64GB - Đen</td>
                            <td><img src="https://cdn2.cellphones.com.vn/insecure/rs:fill:50:50/q:90/plain/https://cellphones.com.vn/media/catalog/product/d/i/dien-thoai-meizu-mblu-21-denn.jpg" alt="Điện thoại Meizu Mblu 21 4GB 64GB - Đen" onError="this.style.display='none'; this.nextElementSibling.style.display='flex';"><div class="no-image" style="display:none;"><span>Ảnh lỗi</span></div></td>
                            <td class="price-cell">1.990.000&nbsp;₫</td>
                        </tr>
            
                        </tbody>
                    </table>
                </div>
        
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
    
