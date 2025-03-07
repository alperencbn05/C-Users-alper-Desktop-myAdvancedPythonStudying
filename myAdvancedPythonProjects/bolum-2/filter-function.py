sayilar = [1,3,5,-4,-3]

def negatifSayilar(x):
    if x < 0:
        return True
    else:
        return False

sonuc = list(filter(negatifSayilar , sayilar))
print(sonuc)

sonuc = list(filter(lambda x: x<0 , sayilar))
sonuc = list(filter(lambda x: x%2 == 0 ,sayilar))
print(sonuc)


isimler = ["çınar" , "ali" ,"ada" , "yiğit" ,"sena"]


sonuc = list(map(lambda x: x.upper() ,(filter(lambda x: x[0] == "a" , isimler)) ))
print(sonuc)

users = [
    {"username" : "AlperenCoban" , "posts" : ["post1 " , "post2"]} ,
    {"username" : "DusanTadic" , "posts" : ["post1 " , "post2" , "post3"]} ,
    {"username" : "LionelMessi" , "posts" : ["post1 "]} 
]


filteredUser = list(filter(lambda u: len(u["posts"]) >2 , users))
sonuc = list(map(lambda u: u["username"] , filteredUser))
print(sonuc)