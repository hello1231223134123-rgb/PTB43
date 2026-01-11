import math 
# imput: a,b 
a =0 
b = 0
while(a and b ) == 0  : 
    a = int(input("nhap tu so: "))
    b = int(input("nhap mau so: "))
# tinh boi chung nho nhat 
bcnm = math.lcm(a,b)
print (f"BCNM cua {a} va {b} la: {bcnm}")
# rut gon phan so (ucln)
print(F"phan so ban dau: {a}/{b}")
ucln = math.gcd(a, b)
a = a // ucln 
b = b // ucln
print (f"phan so rut gon: {a}/{b}")
