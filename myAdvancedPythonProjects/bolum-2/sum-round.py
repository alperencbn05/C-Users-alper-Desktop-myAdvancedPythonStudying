sayilar = [1,3,5,4,32,56]

sonuc = sum(sayilar , 15)

print(sonuc)

products = [
    {"title" :"samsung s23" , "price" : 80000},
    {"title" :"iphone 15" , "price" : 30020},
    {"title" :"samsung a50" , "price" : 41212},
    {"title" :"samsung a50" , "price" : 0}

]

toplamFiyat = sum([product["price"] for product in products])
urunAdeti  = len([(urun)  for urun in products if urun["price"] > 0])
ortalama = toplamFiyat / urunAdeti
print(round(ortalama))