sayilar = [1,2,3,4,5,6]

# kareleri = []

# for sayi in sayilar:
#     kareleri.append(sayi **2)

# print(kareleri)


# def kareAl(sayi):
#     return sayi ** 2

sonuc = list(map(lambda sayi: sayi ** 2, sayilar))
print(sonuc)


sayilar = ["1","2","3","4","5","6"]
# int("2") # 2
sonuc = list(map(int , sayilar))


isimler = ["ali" , "hasan" , "ayşe" , "zeynep"]

sonuc = list(map(str.capitalize , isimler))
print(sonuc)

kullanicilar = [
{"ad":"ali" , "soyad" : "yılmaz"},
{"ad":"alperen" , "soyad" : "coban"}
]

sonuc = list(map(lambda kisi: kisi["ad"] , kullanicilar))
print(sonuc)