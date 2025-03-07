# any all

sonuc = all([True , True , False])
sonuc = any([True , False , True])

# And --> true and true all()
# Or --> True or flase --> any()


sayilar = [1,3,5,7,6,52,0]

sonuc = [bool(sayi) for sayi in sayilar]
sonuc = any([bool(sayi) for sayi in sayilar])

sonuc = all([sayi % 2 == 0 for sayi in sayilar])

users = ["ahmet" , "çınar" ,"ali"]

sonuc = all([user[0] == "a" for user in users])
sonuc = any([user[0] == "a" for user in users])

print(sonuc)