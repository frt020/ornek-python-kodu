print("""bu programda büşra, ahmet, zeynep, yusuf, ayşe ve mehmet isimlerinin girebilirsiniz\n\tgirilen ismin Türkiyede kac kişinin kulandığını söyleyen kod\n""")

while True:
    isim_sayısı = input("BİR İSİM GİRİNİZ (cıkmak icin 'q' basın) :")
    if isim_sayısı == "q":
        print("programdan cıkıldı")
        break
    isim_sayısı = isim_sayısı.upper()
    if isim_sayısı == "BÜŞRA":
        print("Türkiyede Büşra ismini kulanan kişi sayısı= 203.846 dir")
    elif isim_sayısı == "AHMET":
        print("Türkiyede Ahmet ismini kulanan kişi sayısı= 897.911 dir")
    elif isim_sayısı == "ZEYNEP":
        print("Türkiyede Zeynep ismini kulanan kişi sayısı= 646.839 dir")
    elif isim_sayısı == "YUSUF":
        print("Türkiyede Yusuf ismini kulanan kişi sayısı= 498.322 dir")
    elif isim_sayısı == "AYŞE":
        print("Türkiyede Ayşe ismini kulanan kişi sayısı= 968.897 dir")
    elif isim_sayısı == "MEHMET":
        print("Türkiyede Mehmet ismini kulanan kişi sayısı= 2 milyon 826 bin 306 dir")
    else:
        print("lütfen sadece büşra, ahmet, zeynep, yusuf, ayşe ve mehmet isimlerini giriniz""\nve sayı girmeyiniz")