#tao tam giac vuong * voi n dong (>1)
#input n
n = input("so dong > 1: ") #str
n = int(n) #
if (n < 2):
    print("so dong phai lon hon 1 ")
else: 
    for i in range(1, n+1 ):
        print("*"*i)
