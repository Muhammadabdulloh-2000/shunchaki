# 01:
print('Besh xonali son uchun dastur!')
a = 54321 #int(input('Ixtiyoriybesh xonali son kiriting: '))
# b = a // 10000
# c = a % 10000
# d = c // 1000
# k = c % 1000
# e = k // 100
# f = k % 100
# g = f // 10
# h = f % 10
# i = b + d + e + g + h

b = a % 10
d = a // 10 % 10
e = a // 100 % 10
g = a // 1000 % 10
h = a // 10000 % 10
i = b + d + e + g + h
print("Besh xonali sonni 1chi raqami: ",b)
print("Besh xonali sonni 2chi raqami: ",d)
print("Besh xonali sonni 3chi raqami: ",e)
print("Besh xonali sonni 4chi raqami: ",g)
print("Besh xonali sonni 5chi raqami: ",h)
print("Besh xonali sonlar yig'indisi: ",i)

