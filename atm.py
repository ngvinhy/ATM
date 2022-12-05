def atm(tk, password, tien, gioihan, pin, changesodu, changehanmuc, sodu_atm, stt):
    from tracuu import chucnang1
    from ruttien import chucnang2
    from chuyentien import chucnang3
    from doimapin import chucnang4
    header = '********************'
    dem = 1
    mapin = int(input('MÃ PIN: '))
    while dem <= 3:
        if mapin == password:
            break
        if dem == 3:
            print(header.center(39))
            print('   SAI MÃ PIN QUÁ SỐ LẦN QUY ĐỊNH!!!\nTHẺ CỦA BẠN SẼ BỊ KHÓA TRONG ÍT PHÚT!!!')
            print(header.center(39))
            exit()
        else:
            mapin = int(input(f'MÃ PIN KHÔNG HỢP LỆ (CÒN {3-dem} LẦN THỬ): '))
            dem += 1
    print(header.center(27))
    print('BẠN ĐÃ ĐĂNG NHẬP THÀNH CÔNG')
    print(header.center(27))
    while True:
        if sodu_atm[0] <= 0:
            print(header.center(42))
            print('SỐ DƯ ATM ĐÃ HẾT, XIN VUI LÒNG THỬ LẠI SAU')
            print(header.center(42))
            break
        print('*1. Tra cứu tài khoản\n*2. Rút tiền\n*3. Chuyển tiền\n*4. Thay đổi mã PIN\n*0. Thoát')
        chucnang = str(input('CHỌN CHỨC NĂNG BẠN MUỐN SỬ DỤNG: '))
        if chucnang == '1':
            chucnang1(header, tk, tien, gioihan)
            q = str(input('BẠN CÓ MUỐN TIẾP TỤC SỬ DỤNG DỊCH VỤ KHÔNG?\n*1. Có\n*2. Không\nChọn: '))
            if q == '2':
                break
            elif q != '1' and q != '2':
                print(header.center(61))
                print('CHỨC NĂNG KHÔNG HỢP LỆ, BẠN SẼ ĐƯỢC CHUYỂN ĐẾN MÀN HÌNH CHÍNH')
                print(header.center(61))
        elif chucnang == '2':
            chucnang2(header, tk, tien, gioihan, changehanmuc, changesodu, sodu_atm, stt)
            q = str(input('BẠN CÓ MUỐN TIẾP TỤC SỬ DỤNG DỊCH VỤ KHÔNG?\n*1. Có\n*2. Không\nChọn: '))
            if q == '2':
                break
            elif q != '1' and q != '2':
                print(header.center(61))
                print('CHỨC NĂNG KHÔNG HỢP LỆ, BẠN SẼ ĐƯỢC CHUYỂN ĐẾN MÀN HÌNH CHÍNH')
                print(header.center(61))
        elif chucnang == '3':
            chucnang3(header, tien, gioihan, changehanmuc, changesodu, sodu_atm, stt)
            q = str(input('BẠN CÓ MUỐN TIẾP TỤC SỬ DỤNG DỊCH VỤ KHÔNG?\n*1. Có\n*2. Không\nChọn: '))
            if q == '2':
                break
            elif q != '1' and q != '2':
                print(header.center(61))
                print('CHỨC NĂNG KHÔNG HỢP LỆ, BẠN SẼ ĐƯỢC CHUYỂN ĐẾN MÀN HÌNH CHÍNH')
                print(header.center(61))
        elif chucnang == '4':
            chucnang4(header, pin, stt)
            break
        elif chucnang == '0':
            break
        else:
            print(header.center(44))
            print('CHỨC NĂNG KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI')
            print(header.center(44))
