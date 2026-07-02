import json
import os
from src.otsl_to_htlml import convert_to_html

# Đường dẫn file json (bây giờ nó đã ở thư mục gốc SPRINT)
json_file = 'results.json'

if not os.path.exists(json_file):
    print(f"Lỗi: Không tìm thấy file {json_file}")
    exit()

with open(json_file, 'r') as f:
    results = json.load(f)

# Tạo thư mục đầu ra
if not os.path.exists('output_html'):
    os.makedirs('output_html')

for filename, otsl_str in results.items():
    try:
        # Chuyển đổi (R=10, C=5 là giả định, bạn có thể điều chỉnh)
        html_code = convert_to_html(otsl_str, R=10, C=5)
        out_name = filename.replace('.png', '.html')
        with open(f"output_html/{out_name}", "w") as f:
            f.write(html_code)
        print(f"Đã tạo: output_html/{out_name}")
    except Exception as e:
        print(f"Lỗi khi xử lý {filename}: {e}")