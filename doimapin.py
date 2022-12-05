def chucnang4(header4, pin4, stt4):
    while True:
        oldpin = int(input('NHẬP MÃ PIN CŨ: '))
        if oldpin == pin4[stt4]:
            newpin = int(input('NHẬP MÃ PIN MỚI: '))
            while True:
                newpin1 = int(input('NHẬP LẠI MÃ PIN MỚI: '))
                if newpin == newpin1:
                    pin4[stt4] = newpin
                    print(header4.center(80))
                    print('BẠN ĐÃ THAY ĐỔI THÀNH CÔNG MÃ PIN, XIN VUI LÒNG ĐĂNG NHẬP LẠI ĐỂ SỬ DỤNG DỊCH VỤ')
                    print(header4.center(80))
                    break
                else:
                    print(header4.center(49))
                    print('MÃ PIN MỚI KHÔNG TRÙNG KHỚP, XIN VUI LÒNG THỬ LẠI')
                    print(header4.center(49))
            break
        else:
            print(header4.center(32))
            print('SAI MÃ PIN, XIN VUI LÒNG THỬ LẠI')
            print(header4.center(32))
