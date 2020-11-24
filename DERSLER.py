#   TÜM DERS NOTLARI
#   NOT-1: KLAVYEDEN DEĞER GİRİŞİ
isim=input("isminizi giriniz:") #kullanıcıdan ismini girmesini istiyoruz
print("-"*10)                   #
print(isim)                     #kullanıcının girdiği değeri ekrana yazıdırıyoruz
print("-"*10)                   #
#   NOT-2: KLAVYEDEN SAYI DEĞERİ GİRİŞİ
#   - Kullanıcının girdiği iki sayının toplanması
sayi1=int(input("İlk sayıyı giriniz :\n"))      # "int" komutunu kullanarak girilen değerleri tam sayıya çeviriyoruz...
sayi2=int(input("İkinci sayıyı giriniz :\n"))   # "\n" komutu kullanıcının girdiği değerleri bir alt satırda girmesini sağlar
toplam=sayi1+sayi2
print("İşleminiz: {0} + {1} = \t {2}".format(sayi1,sayi2,toplam)) #Ekran çıktısı=> "İşleminiz: 3 + 5 =  8" biçiminde yazılabilmesini sağlar
#   NOT-3: KARŞILAŞTIRMA İFADELERİ "IF"
sayi=int(input("Bir sayı giriniz :\t"))
if sayi==10:                                # "==" Eşittir Operatörü
    print("Girilen Sayı ON dur")
if sayi>10:                                 # ">" Büyüktür Operatörü
    print("Girilen Sayı ON dan BÜYÜKTÜR")
if sayi>=10:                                # ">=" Büyük ve Eşittir Operatörü
    print("Girilen Sayı ON dan BÜYÜK ve EŞİTTİR")
if sayi<10:                                 # "<" Küçüktür Operatörü
    print("Girilen Sayı ON dan KÜÇÜKTÜR")
if sayi<=10:                                # "<=" Küçük ve Eşittir Operatörü
    print("Girilen Sayı ON dan KÜÇÜK ve EŞİTTİR")
if sayi != 10:                              # "!=" Eşittir Operatörü
    print("Girilen Sayı ON dan FARKLIDIR")
#   NOT-4: DÖNGÜLER-"WHILE" KOMUTU
#   -Ekrana 0 dan başlayarak 10 'a olan sayıları alt alta yazar
say=0                                       # başlangıç değeri
while say<11:                               # while komutu kendinden sonra belirtilen şart doğru olduğu sürece..
    print(say)                              #   altındaki girintide belirtilen ifadeleri tekrar eder
    say=say+1
#   "WHILE" komutuyla ilgili örnekler
#   -ORNEK-1- 1 ile 100 arasındaki sayıları alt alta yazdırma
sayi=1;
while sayi<=100:
    print(sayi)
    sayi=sayi+1                             # bunun yerine  "sayi+=1" de kullanılabilir
#   -ORNEK-2- 100 den 1'e kadar olan sayıları ters sırada alt alta yazdırma
sayi=100;
while sayi>=1:
    print(sayi)
    sayi -= 1
#   -ORNEK-3- 1 ile 100 arasındaki tek sayıları alt alta yazdırma
sayi=1;
while sayi<=100:
    if (sayi%2)==1:
        print(sayi)
    sayi += 1
#   -ORNEK-4- 1 ile 100 arasındaki çift sayıları sayan program
sayi=1;
count=0;
while sayi<=100:
    if (sayi%2)==1:
        count+=1
    sayi += 1
#   -ORNEK-5- kullanıcı 99'dan büyük bir sayı girene kadar girilen sayıları toplayan program
sayi=0
toplam=0
while sayi<100:
    sayi=int(input("Eklenecek Sayıyı giriniz"))
    if  sayi<100:
        toplam+=sayi
    sayi+=1
print("Girdiğiniz sayıların toplamı = \t{toplam}".format(toplam))
#   -ORNEK-6- Örnek 5 in farklı bir yapılış biçimi
kontrol=0
toplam=0
while kontrol<1:
    sayi=int(input("Eklenecek Sayıyı giriniz"))
    if  sayi<100:
        toplam+=sayi
    else:
        kontrol=1                                   # Girilen sayı 99 dan büyük olduğunda kontrol değişkenin değeri "1"...
    sayi +=1                                        # yapılarak "while kontrol<1:" satırındaki şart bozulmuştur.
print("Girdiğiniz sayıların toplamı = \t{toplam}".format(toplam))
#   -ORNEK-7- Birden fazla "While" komutu kullanılarak "*" simgesinden belirtilen boyutta kare oluşturma
boyut=int(input("Karenin Boyutunu Belirtiniz: \t"))
say=0
while say<boyut:
    print("*"*boyut)
    say=say+1
#   -ORNEK-8- Birden fazla "While" komutu kullanılarak "*" simgesinden belirtilen boyutta üçgen oluşturma
boyut=int(input("Üçgenin taban Boyutunu Belirtiniz: \t"))
say=0
while say<boyut:
    print("*"*say)
    say=say+1
#   NOT-5: DÖNGÜLER-"FOR" KOMUTU




