# for item in liste:
#     if (kosul):
#         expression
# [expression for item in liste if]


sayilar = [3,5,7,6,56,34]
sonuc = []

# for sayi in sayilar:
#     if(sayi % 2 == 0):
#         sonuc.append(sayi)


sonuc = [sayi for sayi in sayilar if (sayi % 2 == 0)]
sonuc = [sayi if sayi % 2 == 0 else "tek sayı" for sayi in sayilar]
print(sonuc)


urunFiyatlari = [3000,1000,4000,5000]
vergiler = []

for fiyat in urunFiyatlari:
    if (fiyat > 1000):
        vergiler.append(fiyat * 1.20)




vergiler =[fiyat*1.20 for fiyat in urunFiyatlari if (fiyat > 1000)]
print(vergiler)

vergiler = [fiyat*1.18 if (fiyat>1000) else fiyat*1.10 for fiyat in urunFiyatlari]
print(vergiler)