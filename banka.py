bakiye = 1000
limit = 2000
gecmis = []

while True:
    
    print("1 - Bakiye Görüntüle")
    print("2 - Limit Ayarları")
    print("3 - Para Yatır")
    print("4 - Para Çek")
    print("5 - Para Transferi")
    print("6 - İşlem Geçmişi")
    print("7 - Çıkış")

    islem = int(input("Yapmak istediğiniz İşlem: "))

    if islem == 1:
        print(bakiye)
    
    
    elif islem == 2:
        print(f"Mevcut Günlük Çekim Limitiniz {limit}")
        yenilimit = int(input("Yeni Limit Giriniz: "))
        limit = yenilimit
        gecmis.append(f"Günlük Limit {yenilimit} olarak Ayarlandı!")
    
    elif islem == 3:
        miktar = int(input("Yatırmak İstediğiniz Miktar: "))
        bakiye += miktar
        print(f"Para Yatırma İşlemi Tamamlandı! Yeni Bakiyeniz: {bakiye}")
        gecmis.append(f"Hesaba {miktar}TL Başarıyla Yatırıldı!")
    
    
    elif islem == 4:
        cek = int(input("Çekmek İstediğiniz Miktar: "))
    
        if cek > limit:
            print("Günlük Çekim Limitiniz Yetersiz!")
    
        elif cek > bakiye:
            print("Bakiyeniz Yetersiz!")
        
        else:
            bakiye -= cek
            print(f"Para Çekme İşlemi Tamamlandı! Yeni Bakiyeniz: {bakiye}")
            gecmis.append(f"Hesaptan {cek}TL Başarıyla Çekildi!")
        
    elif islem == 5:
        transfer = int(input("Transfer Edeceğiniz Miktar: "))
    
        if transfer > bakiye:
            print("Bakiyeniz Yetersiz!")
        
        else:
            bakiye -= transfer
            print(f"Transfer Başarıyla Gerçekleştirildi! Yeni Bakiyeniz: {bakiye}")
            gecmis.append(f"{transfer}TL Başarıyla Transfer Edildi!")
        
    elif islem == 6:
        for i in (gecmis):
            print(i)
     
    elif islem == 7:
        print("başarıyla Çıkış Yapıldı!")
        break
    else:
        print("Geçersiz İşlem")
           
    
    