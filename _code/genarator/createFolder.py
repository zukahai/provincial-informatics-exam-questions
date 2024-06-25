import os

# Danh sách các tỉnh thành
provinces = [
    "An Giang", "Bà Rịa - Vũng Tàu", "Bạc Liêu", "Bắc Giang", "Bắc Kạn", "Bắc Ninh", "Bến Tre", "Bình Định",
    "Bình Dương", "Bình Phước", "Bình Thuận", "Cà Mau", "Cao Bằng", "Cần Thơ", "Đà Nẵng", "Đắk Lắk", "Đắk Nông",
    "Điện Biên", "Đồng Nai", "Đồng Tháp", "Gia Lai", "Hà Giang", "Hà Nam", "Hà Nội", "Hà Tĩnh", "Hải Dương", 
    "Hải Phòng", "Hậu Giang", "Hòa Bình", "Hưng Yên", "Khánh Hòa", "Kiên Giang", "Kon Tum", "Lai Châu", "Lâm Đồng",
    "Lạng Sơn", "Lào Cai", "Long An", "Nam Định", "Nghệ An", "Ninh Bình", "Ninh Thuận", "Phú Thọ", "Phú Yên",
    "Quảng Bình", "Quảng Nam", "Quảng Ngãi", "Quảng Ninh", "Quảng Trị", "Sóc Trăng", "Sơn La", "Tây Ninh", "Thái Bình",
    "Thái Nguyên", "Thanh Hóa", "Thừa Thiên - Huế", "Tiền Giang", "TP. Hồ Chí Minh", "Trà Vinh", "Tuyên Quang",
    "Vĩnh Long", "Vĩnh Phúc", "Yên Bái"
]

# Tạo folder và file readme.md cho từng tỉnh thành
for province in provinces:
    # Tạo thư mục chính cho tỉnh
    # province = '../' + province
    os.makedirs(province, exist_ok=True)
    
    # Tạo file readme.md
    readme_path = os.path.join(province, 'readme.md')
    with open(readme_path, 'w') as f:
        f.write(f"# Đề {province}\n\nPhía trên là các đề thi tỉnh {province} đã thu thập được, có thể còn nhiều thiếu sót, nếu bạn có đề thi của tỉnh này, hãy đóng góp để mọi người cùng có lợi ích nhé.\n\nĐóng góp đề thi [Tại đây](https://forms.gle/AeP6nuRsy4whT1rF7)")

    # Tạo các thư mục cho Lớp 10, Lớp 11, Lớp 12 nếu chúng chưa tồn tại
    for grade in ["Lớp 10", "Lớp 11", "Lớp 12"]:
        os.makedirs(os.path.join(province, grade), exist_ok=True)

print("Đã tạo xong các folder và file readme.md.")
