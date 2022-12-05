def chucnang2(header2, tk2,  tien2, gioihan2, changehanmuc2, changesodu2, sodu_atm2, stt2):
    while True:
        if gioihan2 == 0:
            print(header2.center(43))
            print('HẠN MỨC GIAO DỊCH TRONG NGÀY CỦA BẠN ĐÃ HẾT')
            print(header2.center(43))
            break
        else:
            ruttien = int(input('NHẬP SỐ TIỀN CẦN RÚT: '))
            if ruttien <= 0:
                print(header2.center(42))
                print('SỐ TIỀN KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI')
                print(header2.center(42))
            elif ruttien > sodu_atm2[0]:
                print(header2.center(60))
                print('ATM KHÔNG ĐỦ SỐ DƯ THỰC HIỆN GIAO DỊCH, XIN VUI LÒNG THỬ LẠI')
                print(header2.center(60))
            elif ruttien <= tien2:
                if gioihan2 < ruttien:
                    print(header2.center(67))
                    print('SỐ TIỀN VƯỢT QUÁ HẠN MỨC GIAO DỊCH TRONG NGÀY, XIN VUI LÒNG THỬ LẠI')
                    print(header2.center(67))
                else:
                    if ruttien % 50000 == 0:
                        tien2 = tien2 - ruttien
                        changesodu2[stt2] = tien2
                        sodu_atm2[0] -= ruttien
                        gioihan2 = gioihan2 - ruttien
                        changehanmuc2[stt2] = gioihan2
                        while True:
                            bienlai = str(input('BẠN CÓ MUỐN NHẬN HÓA ĐƠN KHÔNG?\n*1. Có\n*2. Không\nChọn: '))
                            if bienlai == '1':
                                print(header2.center(27))
                                print(f'CHỦ THẺ: {tk2}\nSỐ TIỀN ĐÃ RÚT: {ruttien} VNĐ\nSỐ DƯ: {tien2} VNĐ')
                                print(header2.center(27))
                                break
                            elif bienlai == '2':
                                print(header2.center(48))
                                print('GIAO DỊCH HOÀN THÀNH, XIN VUI LÒNG ĐỢI NHẬN TIỀN')
                                print(header2.center(48))
                                break
                            else:
                                print(header2.center(44))
                                print('CHỨC NĂNG KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI')
                                print(header2.center(44))
                    else:
                        print(header2.center(68))
                        print('SỐ TIỀN GIAO DỊCH PHẢI LÀ BỘI SỐ CỦA 50000 VNĐ, XIN VUI LÒNG THỬ LẠI')
                        print(header2.center(68))
            else:
                print(header2.center(36))
                print('SỐ DƯ KHÔNG ĐỦ, XIN VUI LÒNG THỬ LẠI')
                print(header2.center(36))
