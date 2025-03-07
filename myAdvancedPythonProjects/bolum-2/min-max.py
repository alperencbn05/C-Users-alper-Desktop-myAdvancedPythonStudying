sayilar = [1,4,5]
isimler = ["ahmet" ,  "alperen" ,"ali"]


# sonuc = min(sayilar)
# sonuc = min(isimler)
# print(sonuc)



# sonuc = min([len(isim) for isim in isimler])
# print(min)

sonuc = max(isimler , key = lambda isim: len(isim))
sonuc = min(isimler , key = lambda isim: len(isim))


print(sonuc)

urunler = [
    {"title" :"samsung s23" , "price" : 80000},
    {"title" :"iphone 15" , "price" : 30020},
    {"title" :"samsung a50" , "price" : 41212},

]

sonuc = min(urunler , key = lambda urun: urun["price"])
print(sonuc["price"])


max = 0

for urun in urunler:
    if(urun["price"] > max):
        max = urun["price"]


print(max)