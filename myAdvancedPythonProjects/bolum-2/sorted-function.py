sayilar = [1,53,4,5,76,23]

# sayilar.sort()

# print(sayilar)

print(sorted(sayilar , reverse=True)) # yeni liste döndütür


users = [
{"username" : "josemorunhio" , "posts": ["post 1" , "post 2"] , "email" : "jose@gmail.com"},
{"username" : "dominiclivakovic" , "posts": ["post 1" , "post 2" , "post 3"] , "email" : "dominic@gmail.com"},
{"username" : "skriniar" , "posts": [] , "email" : "skriniar@gmail.com"},
{"username" : "mertHakanYandas" , "posts": ["post 1" , "post 2" , "post 3" , "post 4" , "post 5"]}
]


sonuc1 = sorted(users , key=lambda user: user["username"])
sonuc2 = sorted(users , key=lambda user: len (user["posts"]) , reverse=True)

sonuc = list(map(lambda user: user["username"] , sonuc2 ,))


print(sonuc )

