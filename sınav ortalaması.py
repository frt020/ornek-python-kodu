
print("\t""\t""girilen sınavların ortalamasını bulan kod")
print("\n")
sayi1=float(input("1 SINAVINI gir :"))
sayi2=float(input("2 SINAVINI gir :"))
sayi3=float(input("3 SINAVINI gir :"))

ortalama=(sayi1+sayi2+sayi3)/3

print("SINAV ORTALAMASI",ortalama)
if ortalama >= 85:
    print("sınıfı TAKTİR ile gectiniz")
elif ortalama < 84 and ortalama >= 60:
    print("sınıfı TEŞEKÜR ile gectiniz")
elif ortalama < 59 and ortalama >= 50:
    print("sınıfı gectiniz")
else:
    print("sınıfta KALDINIZ")

