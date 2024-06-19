import pandas as pd
from download import download_file_from_google_drive, get_unique_file_name
import os
import json
from write_readme import write_readme

# Đường dẫn đến file CSV
file_path = './_code/' + 'Đóng góp đề thi - Câu trả lời biểu mẫu 1.csv'

contrubute = {};
# Đọc file contrubute.json
if os.path.exists('./_code/contrubute.json'):
    with open('./_code/contrubute.json', 'r') as f:
        contrubute = json.loads(f.read())

# Đọc file CSV
data = pd.read_csv(file_path)

for index, row in data.iterrows():
    if row['Đã duyệt'] == False:
        tinh = row['Bạn đang muốn đóng góp đề của tỉnh nào?']
        lop = row['Đề thi dành cho lớp nào?']
        nam = row['Năm tổ chức thi']
        link = row['Đề thi (Nên là file pdf hoặc ảnh)']
        email = row['Email']
        print(f'Tỉnh: {tinh}, Lớp: {lop}, Năm: {nam}, Link: {link}')

        path = f'{tinh}/{lop}/{nam}/'
        # Tao thu muc neu chua ton tai
        if not os.path.exists(path):
            os.makedirs(path)
            # Tao file README.md
            with open(path + 'README.md', 'w') as f:
                f.write(f'# {tinh} - {lop} - {nam}\n\n')
                f.write(f'Đề thi dành cho lớp {lop} tỉnh {tinh} năm {nam}\n\n')
                f.write('## Danh sách đề thi\n\n')
        name_file = f'{tinh} - {lop} - {nam}.pdf'
        id = link.split('id=')[1]

        # Nếu tỉnh đã tồn tại thì đổi tên
        if os.path.exists(path + name_file):
            name_file = get_unique_file_name(path, tinh, lop, nam)


        download_file_from_google_drive(id, path + name_file)

        # Ghi thông tin vào file README.md
        with open(path + 'README.md', 'a') as f:
            name_file_link = name_file.replace(' ', '%20')
            f.write(f'- [{name_file}]({name_file_link})\n')
            f.write(f'Email: {email}\n')
            f.write('\n')

        if email in contrubute:
            contrubute[email] += 1
        else:
            contrubute[email] = 1

        # Lưu contrubute vào file contrubute.json
        with open('./_code/contrubute.json', 'w') as f:
            f.write(json.dumps(contrubute))

        write_readme()
            


