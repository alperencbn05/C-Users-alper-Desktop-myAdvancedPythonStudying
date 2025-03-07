# lambda arguments: expression

def kareAl(a):
    return a**2


sonuc = (lambda a: (a ** 2))(3)

kareAl = (lambda a: (a ** 2))
print(kareAl(4))



toplama = lambda a,b,c: a + b + c

sonuc = toplama(1,2,3)

print(sonuc)


def myFunc(n):
    return lambda a: a * n

carpma2 = myFunc(2)
carpma3 = myFunc(3)

print(carpma3(6))