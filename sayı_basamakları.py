print("\n")

print("\t""\t""....girilen sayının basamak değerini bulan kod....")
print("\t""\t"".....en fazla 9 basamaklı bir sayı girebilirsin!....")

print("\n")

toplam = int(input(" bir sayı girin : "))
if toplam > 1 and toplam < 9:
    print("BİRLER BASAMAĞI")
elif toplam > 10 and toplam < 99:
    print("ONLAR BASAMAĞI")
elif toplam > 100 and toplam < 999:
    print("YÜZLER BASAMAĞI")
elif toplam >= 1000 and toplam < 9999:
    print("BİNLER BASAMAĞI")
elif toplam > 10000 and toplam < 99999:
    print("ON BİNLER BASAMAĞI")
elif toplam > 100000 and toplam < 999999:
    print("YÜZ BİNLER BASAMAĞI")
elif toplam > 1000000 and toplam < 9999999:
    print("MİLYONLAR BASAMAĞI")
elif toplam > 10000000 and toplam < 99999999:
    print("ON MİLYONLAR BASAMAĞI")
elif toplam > 100000000 and toplam < 999999999:
    print("YÜZ MİLYONLAR BASAMAĞI")
else:
    print("en fazla 9 basamaklı bir sayı girebilirsin")
   
     