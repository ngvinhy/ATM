from atm import atm
from dulieu import tenkh, tentk, mk, sodu, hanmuc, sodunganhang
giaodien = '***************'
if sodunganhang[0] <= 0:
    exit()
while True:
    name = str(input('VUI LÒNG NHẬP TÊN ĐĂNG NHẬP: '))
    if name in tentk:
        i = tentk.index(name)
        atm(tenkh[i], mk[i], sodu[i], hanmuc[i], sodu, hanmuc, i, sodunganhang, mk)
    else:
        print(giaodien.center(27))
        print('TÊN ĐĂNG NHẬP KHÔNG HỢP LỆ')
        print(giaodien.center(27))
