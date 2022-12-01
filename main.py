from atm import atm
title = 'CHƯƠNG TRÌNH GIAO DỊCH TẠI CÂY ATM'
print(title.center(60))
# giả sử list người dùng chỉ có 5 thành viên trong nhóm
tenkh = ['Nguyễn Vĩnh Ý', 'Nguyễn Thị Thu Hiền', 'Đinh Hồng Cơ', 'Bùi Đăng Nguyên', 'Đỗ Thành Danh']
tentk = ['y', 'hien', 'co', 'nguyen', 'danh']
mk = [1, 2, 3, 4, 5]
sodu = [30000000, 40000000, 50000000, 60000000, 70000000]
hanmuc = [5000000, 10000000, 15000000, 20000000, 30000000]
# giả sử ngân hàng có 10 triệu
nganhang = [10000000]
while True:
    name = str(input('Hãy nhập tên tài khoản: '))
    if name in tentk:
        i = tentk.index(name)
        atm(tenkh[i], mk[i], sodu[i], hanmuc[i], sodu, hanmuc, i, nganhang)
    if nganhang[0] <= 0:
        break
