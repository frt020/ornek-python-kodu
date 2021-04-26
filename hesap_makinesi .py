print("_"*90)
print("\n")

print("\t""\t""...HESAP MAKİNESİ = sadece,  toplama,  bölme,  carpma,  cıkarma...""\n"
"\t""\t""\t""\t""...işlemi yapılır örnek kod...""\n","_"*90)


print("1.CARPMA")
print("2.BÖLME")
print("3.TOPLAMA")
print("4.CIKARMA")
# yukarı bölüm süsleme -----------------------------------------


try:
    while True:
        a = input("""YAPILACAK İŞLEMİ SECİN (CIKMAK İCİN 'q'): """)

        if a == "q":
            print("\n""PROGRAMDAN CIKILDI""\n")
            break
        
        elif a == "1":
            carpma = int(input("birinci sayıyı giriniz : "))
            carpma1 = int(input("ikinci sayıyı giriniz : "))
            print("\n""SONUC",carpma,"*",carpma1,"=",carpma * carpma1,"\n")
            

        elif a == "2":
            bölme = int(input("birinci sayıyı giriniz: "))
            bölme1 = int(input("ikinci sayıyı giriniz: "))
            print("\n""SONUC",bölme,"/",bölme1,"=",bölme / bölme1,"\n")

    
    
        elif a == "3":
            toplama = int(input("birinci sayıyı giriniz: "))
            toplam1 = int(input("ikinci sayıyı giriniz : "))
            print("\n""SONUC",toplama,"+",toplam1,"=",toplama + toplam1,"\n")
            
    
        elif a == "4":
            cıkarma = int(input("ilk sayıyı giriniz : "))
            cıkarma1 = int(input("ikinci sayıyı giriniz : "))
            print("\n""SONUC",cıkarma,"-",cıkarma1,"=",cıkarma - cıkarma1,"\n")

        else:
            print("\n""lütfen sadece sayı giriniz ve 4 üstü sayılar girmeyiniz..""\n")


except ValueError:
    print("\n""lütfen sadece sayı giriniz""\n")

except ZeroDivisionError:
        print("\n",bölme,"SAYISI SIFIRA BÖLÜNEMEZ""\n")
        
    

        
    