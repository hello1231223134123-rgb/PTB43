#-------------------------------------------------------
#khai bao sau ki tu 
chuoi_rong ="" 
fullname =  "Hoang Hai Nam "
print(len(chuoi_rong))
print(len(fullname))
#-------------------------------------------------------
#duyet xau 
#truy cap phan tu 
for chart in fullname:
 print(chart,end="")

for index in range(len(fullname)):
 #truy cap phan tu 
 print(f"{index}:{fullname[index]}")
#-------------------------------------------------------
# noi xau 
sentence = "My fullname is " + fullname + "."
print(sentence)
#-------------------------------------------------------
#xau con
firstname = "Hoang"
lastname = "Nam"
#--------------------------------------------------------
#tim xau con trong danh sach (in)
print(fullname.lower())
print(fullname.upper())
print(fullname.capitalize())
#---------------------------------------------------------
#tim xau con (find )
d_index = fullname.find("d")
print(d_index)
#NOTE:find(ki tu can tim sart stop )
k_index = fullname.find("k",4)
print(k_index)
#---------------------------
#str->list
namelist = fullname.split(" ")
print(namelist)
#----------------------------------------------------------
#thay doi phan tu (gia tri)
#NOTE:neu khong co <so luong can thay -> sua het 
newName = fullname.replace("Nam", "Namm")
print(newName)