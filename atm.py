def atm(tk, password, tien, gioihan, changesodu, changehanmuc, stt, sodu_atm, pin):
    giaodien = '***************'
    dem = 1
    mapin = int(input('MÃ PIN: '))
    while dem <= 3:
        if mapin == password:
            break
        if dem == 3:
            print(giaodien.center(39))
            print('   SAI MÃ PIN QUÁ SỐ LẦN QUY ĐỊNH!!!\nTHẺ CỦA BẠN SẼ BỊ KHÓA TRONG ÍT PHÚT!!!')
            print(giaodien.center(39))
            exit()
        else:
            mapin = int(input(f'MÃ PIN KHÔNG HỢP LỆ (CÒN {3-dem} LẦN THỬ): '))
            dem += 1
    print(giaodien.center(27))
    print('BẠN ĐÃ ĐĂNG NHẬP THÀNH CÔNG')
    print(giaodien.center(27))
    while True:
        print('*1. Tra cứu tài khoản\n*2. Rút tiền\n*3. Chuyển tiền\n*4. Thay đổi mã PIN\n*0. Thoát')
        chucnang = str(input('CHỌN CHỨC NĂNG BẠN MUỐN SỬ DỤNG: '))
        if chucnang == '1':
            print(giaodien.center(27))
            print(f'CHỦ THẺ: {tk} \nSỐ DƯ: {tien} VNĐ \nHẠN MỨC GIAO DỊCH: {gioihan} VNĐ')
            print(giaodien.center(27))
            q = str(input('BẠN CÓ MUỐN TIẾP TỤC SỬ DỤNG DỊCH VỤ KHÔNG?\n*1. Có\n*2. Không\nChọn: '))
            if q == '2':
                break
        elif chucnang == '2':
            ruttien = int(input('NHẬP SỐ TIỀN CẦN RÚT: '))
            if ruttien <= 0:
                print(giaodien.center(42))
                print('SỐ TIỀN KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI')
                print(giaodien.center(42))
            elif ruttien > sodu_atm[0]:
                print(giaodien.center(60))
                print('ATM KHÔNG ĐỦ SỐ DƯ THỰC HIỆN GIAO DỊCH, XIN VUI LÒNG THỬ LẠI')
                print(giaodien.center(60))
            elif ruttien <= tien:
                if gioihan < ruttien:
                    print(giaodien.center(67))
                    print('SỐ TIỀN VƯỢT QUÁ HẠN MỨC GIAO DỊCH TRONG NGÀY, XIN VUI LÒNG THỬ LẠI')
                    print(giaodien.center(67))
                else:
                    if ruttien % 50000 == 0:
                        tien = tien - ruttien
                        changesodu[stt] = tien
                        sodu_atm[0] -= ruttien
                        gioihan = gioihan - ruttien
                        changehanmuc[stt] = gioihan
                        if gioihan == 0:
                            print(giaodien.center(43))
                            print('HẠN MỨC GIAO DỊCH TRONG NGÀY CỦA BẠN ĐÃ HẾT')
                            print(giaodien.center(43))
                        bienlai = str(input('BẠN CÓ MUỐN NHẬN HÓA ĐƠN KHÔNG?\n*1. Có\n*2. Không\nChọn: '))
                        if bienlai == '1':
                            q = str(input('BẠN CÓ MUỐN TIẾP TỤC SỬ DỤNG DỊCH VỤ KHÔNG?\n*1. Có\n*2. Không\nChọn: '))
                            if q == '1':
                                print(giaodien.center(27))
                                print(f'CHỦ THẺ: {tk}\nSỐ TIỀN ĐÃ RÚT: {ruttien} VNĐ\nSỐ DƯ: {tien} VNĐ')
                                print(giaodien.center(27))
                            if q == '2':
                                print(giaodien.center(27))
                                print(f'CHỦ THẺ: {tk}\nSỐ TIỀN ĐÃ RÚT: {ruttien} VNĐ\nSỐ DƯ: {tien} VNĐ')
                                print(giaodien.center(27))
                                break
                        elif bienlai == '2':
                            q = str(input('BẠN CÓ MUỐN TIẾP TỤC SỬ DỤNG DỊCH VỤ KHÔNG?\n*1. Có\n*2. Không\nChọn: '))
                            if q == '2':
                                print(giaodien.center(48))
                                print('GIAO DỊCH HOÀN THÀNH, XIN VUI LÒNG ĐỢI NHẬN TIỀN')
                                print(giaodien.center(48))
                                break
                    else:
                        print(giaodien.center(68))
                        print('SỐ TIỀN GIAO DỊCH PHẢI LÀ BỘI SỐ CỦA 50000 VNĐ, XIN VUI LÒNG THỬ LẠI')
                        print(giaodien.center(68))
            else:
                print(giaodien.center(36))
                print('SỐ DƯ KHÔNG ĐỦ, XIN VUI LÒNG THỬ LẠI')
                print(giaodien.center(36))
        elif chucnang == '3':
            stk = int(input('NHẬP SỐ TÀI KHOẢN BẠN MUỐN CHUYỂN TIỀN: '))
            chuyentien = int(input('NHẬP SỐ TIỀN CẦN CHUYỂN: '))
            if chuyentien <= 0:
                print(giaodien.center(42))
                print('SỐ TIỀN KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI')
                print(giaodien.center(42))
            elif chuyentien > sodu_atm[0]:
                print(giaodien.center(60))
                print('ATM KHÔNG ĐỦ SỐ DƯ THỰC HIỆN GIAO DỊCH, XIN VUI LÒNG THỬ LẠI')
                print(giaodien.center(60))
            elif chuyentien <= tien:
                if gioihan < chuyentien:
                    print(giaodien.center(67))
                    print('SỐ TIỀN VƯỢT QUÁ HẠN MỨC GIAO DỊCH TRONG NGÀY, XIN VUI LÒNG THỬ LẠI')
                    print(giaodien.center(67))
                else:
                    if chuyentien % 50000 == 0:
                        tien = tien - chuyentien
                        changesodu[stt] = tien
                        sodu_atm[0] -= chuyentien
                        gioihan = gioihan - chuyentien
                        changehanmuc[stt] = gioihan
                        if gioihan == 0:
                            print(giaodien.center(43))
                            print('HẠN MỨC GIAO DỊCH TRONG NGÀY CỦA BẠN ĐÃ HẾT')
                            print(giaodien.center(43))
                        bienlai = str(input('BẠN CÓ MUỐN NHẬN HÓA ĐƠN KHÔNG?\n*1. Có\n*2. Không\nChọn: '))
                        if bienlai == '1':
                            q = str(input('BẠN CÓ MUỐN TIẾP TỤC SỬ DỤNG DỊCH VỤ KHÔNG?\n*1. Có\n*2. Không\nChọn: '))
                            if q == '1':
                                print(giaodien.center(27))
                                print(f'CHỦ THẺ: {tk}\nĐÃ CHUYỂN {chuyentien} VNĐ ĐẾN STK: {stk}\nSỐ DƯ: {tien} VNĐ')
                                print(giaodien.center(27))
                            if q == '2':
                                print(giaodien.center(27))
                                print(f'CHỦ THẺ: {tk}\nĐÃ CHUYỂN {chuyentien} VNĐ ĐẾN STK: {stk}\nSỐ DƯ: {tien} VNĐ')
                                print(giaodien.center(27))
                                break
                        elif bienlai == '2':
                            q = str(input('BẠN CÓ MUỐN TIẾP TỤC SỬ DỤNG DỊCH VỤ KHÔNG?\n*1. Có\n*2. Không\nChọn: '))
                            if q == '2':
                                print(giaodien.center(48))
                                print('GIAO DỊCH HOÀN THÀNH')
                                print(giaodien.center(48))
                                break
                    else:
                        print(giaodien.center(68))
                        print('SỐ TIỀN GIAO DỊCH PHẢI LÀ BỘI SỐ CỦA 50000 VNĐ, XIN VUI LÒNG THỬ LẠI')
                        print(giaodien.center(68))
            else:
                print(giaodien.center(36))
                print('SỐ DƯ KHÔNG ĐỦ, XIN VUI LÒNG THỬ LẠI')
                print(giaodien.center(36))
        elif chucnang == '4':
            oldpin = int(input('NHẬP MÃ PIN CŨ: '))
            if oldpin == pin[stt]:
                newpin = int(input('NHẬP MÃ PIN MỚI: '))
                newpin1 = int(input('NHẬP LẠI MÃ PIN MỚI: '))
                if newpin == newpin1:
                    pin[stt] = newpin
                    print(giaodien.center(80))
                    print('BẠN ĐÃ THAY ĐỔI THÀNH CÔNG MÃ PIN, XIN VUI LÒNG ĐĂNG NHẬP LẠI ĐỂ SỬ DỤNG DỊCH VỤ')
                    print(giaodien.center(80))
                    break
                else:
                    print(giaodien.center(49))
                    print('MÃ PIN MỚI KHÔNG TRÙNG KHỚP, XIN VUI LÒNG THỬ LẠI')
                    print(giaodien.center(49))
            else:
                print(giaodien.center(32))
                print('SAI MÃ PIN, XIN VUI LÒNG THỬ LẠI')
                print(giaodien.center(32))
        elif chucnang == '0':
            break
        else:
            print(giaodien.center(44))
            print('CHỨC NĂNG KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI')
            print(giaodien.center(44))
