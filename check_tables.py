import os
from bs4 import BeautifulSoup

def check_structure(file_path):
    with open(file_path, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    rows = soup.find_all('tr')
    print(f"--- {file_path} ---")
    print(f"Số dòng (tr): {len(rows)}")
    for i, row in enumerate(rows):
        cells = row.find_all(['td', 'th'])
        print(f"  Dòng {i+1}: {len(cells)} cột")

# Kiểm tra 5 file đầu tiên
output_dir = 'output_html'
for i in range(1, 6):
    file_path = os.path.join(output_dir, f"{i}.html")
    if os.path.exists(file_path):
        check_structure(file_path)