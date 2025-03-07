#1 - (1-100) arasındaki sayılardan 12'e tam bölünebilen sayı listesini oluşturunuz

# sayiListesi = [i for i in range(1, 100) if (i % 12 == 0)]
# print(sayiListesi)

# verilen text içerisindeki rakamları içeren bir liste oluşturunuz
# text = "Hello 12345 World" --> [1,2,3,4,5]

# text = "Hello 12345 World"
# rakamlar = [ i for i in text if i.isdigit()]
# print(rakamlar)

# sicakliklar listesinde bulunan her hava bilgisine göre 4 derecenin altında buzlanma tehlikesi yazınız
# sicakliklar = [20,15,0,-5,-2] --> [20,15,"Buzlanma Tehlikesi","Buzlanma Tehlikesi","Buzlanma Tehlikesi"]

# sicakliklar = [20,15,0,-5,-2]
# buzlanmaListesi = [i if i>4 else "Buzlanma Tehlikesi"  for i in sicakliklar]
# print(buzlanmaListesi)


# 4- ogrenciler ve notlar listelerinde notu 50 den fazla olan kişileri ekrana dict verisinde yazdırınız
# ogrenciler = ["ali" , "ahmet" ,"canan"]
# notlar = [50,60,80]
# --> "{'ahmet' : 60, 'canan' : 80}"

gecenNotlar = {}

# ogrenciler = ["ali" , "ahmet" ,"canan"]
# notlar = [50,60,80]

# sonuc = []
# for i in range(len(ogrenciler)):
#     ogrenciNotu = {ogrenciler[i] : notlar[i]}
#     if notlar[i] > 50:
#         sonuc.append(ogrenciNotu)


# print(sonuc)

# ogrenciler = ["ali" , "ahmet" ,"canan"]
# notlar = [50,60,80]

# sonuc =  [{ogrenciler[i] : notlar[i]} for i in range(len(ogrenciler)) if (notlar[i] > 50)]
# print(sonuc)


# 5- For döngüsüyle yazılan uygulamayı list comprehension ile yazınız

sonuc = []

for x in range(3):
    for y in range(3):
        sonuc.append((x,y))


sonuc = [(x,y) for x in range(3) for y in range(3)]
print(sonuc)