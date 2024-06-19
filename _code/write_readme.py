# đọc README-test.md viết vào README.md

import os
import json

def write_readme():
    contrubute = {};
    # Đọc file contrubute.json
    if os.path.exists('./_code/contrubute.json'):
        with open('./_code/contrubute.json', 'r') as f:
            contrubute = json.loads(f.read())
            # print(contrubute)

    # Đọc file README-test.md
    with open('./README-test.md', 'r') as f:
        readme = f.read()

    # Sắp xếp giảm dần theo số lần đóng góp
    contrubute = dict(sorted(contrubute.items(), key=lambda x: x[1], reverse=True))

    # Ghi vào file README.md
    with open('./README.md', 'w') as f:

        sum_ = sum(contrubute.values())
        f.write(readme)
        f.write(f'Có tổng cộng {sum_} đề thi đã được đóng góp\n\n')
        for email, count in contrubute.items():
            f.write(f'- **{email}**: Đóng góp {count} đề bài. \n')

if __name__ == '__main__':
    write_readme()
