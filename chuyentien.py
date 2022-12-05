def chucnang3(header3, tien3, gioihan3, changehanmuc3, changesodu3, sodu_atm3, stt3):
    while True:
        if gioihan3 == 0:
            print(header3.center(43))
            print('HẠN MỨC GIAO DỊCH TRONG NGÀY CỦA BẠN ĐÃ HẾT')
            print(header3.center(43))
            break
        else:
            stk = int(input('NHẬP SỐ TÀI KHOẢN BẠN MUỐN CHUYỂN TIỀN: '))
            chuyentien = int(input('NHẬP SỐ TIỀN CẦN CHUYỂN: '))
            if chuyentien <= 0:
                print(header3.center(42))
                print('SỐ TIỀN KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI')
                print(header3.center(42))
            elif chuyentien > sodu_atm3[0]:
                print(header3.center(60))
                print('ATM KHÔNG ĐỦ SỐ DƯ THỰC HIỆN GIAO DỊCH, XIN VUI LÒNG THỬ LẠI')
                print(header3.center(60))
            elif chuyentien <= tien3:
                if gioihan3 < chuyentien:
                    print(header3.center(67))
                    print('SỐ TIỀN VƯỢT QUÁ HẠN MỨC GIAO DỊCH TRONG NGÀY, XIN VUI LÒNG THỬ LẠI')
                    print(header3.center(67))
                else:
                    if chuyentien % 50000 == 0:
                        tien3 = tien3 - chuyentien
                        changesodu3[stt3] = tien3
                        sodu_atm3[0] -= chuyentien
                        gioihan3 = gioihan3 - chuyentien
                        changehanmuc3[stt3] = gioihan3
                        while True:
                            bienlai = str(input('BẠN CÓ MUỐN NHẬN HÓA ĐƠN KHÔNG?\n*1. Có\n*2. Không\nChọn: '))
                            if bienlai == '1':
                                print(header3.center(27))
                                print(f'SỐ TÀI KHOẢN NGƯỜI NHẬN: {stk}\nSỐ TIỀN ĐÃ CHUYỂN: {chuyentien} VNĐ\nSỐ DƯ: {tien3} VNĐ')
                                print(header3.center(27))
                                break
                            elif bienlai == '2':
                                print(header3.center(48))
                                print('GIAO DỊCH HOÀN THÀNH')
                                print(header3.center(48))
                            else:
                                print(header3.center(44))
                                print('CHỨC NĂNG KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI')
                                print(header3.center(44))
                    else:
                        print(header3.center(68))
                        print('SỐ TIỀN GIAO DỊCH PHẢI LÀ BỘI SỐ CỦA 50000 VNĐ, XIN VUI LÒNG THỬ LẠI')
                        print(header3.center(68))
            else:
                print(header3.center(36))
                print('SỐ DƯ KHÔNG ĐỦ, XIN VUI LÒNG THỬ LẠI')
                print(header3.center(36))
