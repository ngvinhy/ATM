from atm import atm
giaodien = '***************'
# giả sử list người dùng chỉ có 5 thành viên trong nhóm
tenkh = ['NGUYỄN VĨNH Ý', 'NGUYỄN THỊ THU HIỀN', 'ĐINH HỒNG CƠ', 'BÙI ĐĂNG NGUYÊN', 'ĐỖ THÀNH DANH']
tentk = ['y', 'hien', 'co', 'nguyen', 'danh']
mk = [1234, 2345, 3456, 4567, 5678]
sodu = [30000000, 40000000, 50000000, 60000000, 70000000]
hanmuc = [5000000, 10000000, 15000000, 20000000, 30000000]
# giả sử ngân hàng có sẵn 10 triệu
nganhang = [10000000]
while True:
    name = str(input('VUI LÒNG NHẬP TÊN ĐĂNG NHẬP: '))
    if name in tentk:
        i = tentk.index(name)
        atm(tenkh[i], mk[i], sodu[i], hanmuc[i], sodu, hanmuc, i, nganhang, mk)
    elif nganhang[0] <= 0:
        break
    else:
        print(giaodien.center(27))
        print('TÊN ĐĂNG NHẬP KHÔNG HỢP LỆ')
        print(giaodien.center(27))

