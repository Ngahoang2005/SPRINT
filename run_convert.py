import json
from src.otsl_to_htlml import convert_to_html

# Mở file kết quả suy luận
with open('results.json', 'r') as f:
    results = json.load(f)

# Tạo thư mục chứa file HTML nếu chưa có
import os
os.makedirs('output_html', exist_ok=True)

for filename, otsl_str in results.items():
    # Lưu ý: Các file trong MUSTARD có kích thước khác nhau. 
    # Cần R và C để align chính xác. Nếu không biết, hãy để R, C mặc định (ví dụ 10, 5)
    # hoặc phải lấy từ dữ liệu thực tế.
    try:
        html_code = convert_to_html(otsl_str, R=10, C=5)
        out_name = filename.replace('.png', '.html')
        with open(f"output_html/{out_name}", "w") as f:
            f.write(html_code)
        print(f"Đã tạo: output_html/{out_name}")
    except Exception as e:
        print(f"Lỗi khi xử lý {filename}: {e}")