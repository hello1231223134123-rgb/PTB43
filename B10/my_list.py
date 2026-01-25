danh_sach_1 = [1, "a", "abc123", 12.3 , False]

#----------------------------------------
#duyệt danh sách 
for i in range (len(danh_sach_1)): 
    print(danh_sach_1)
#dung khi khong can index 
for value in danh_sach_1:
    print(value)

#thêm mới phần tử 
#append (value ):them vao cuoi phần 
danh_sach_1.append(100)
print(danh_sach_1)
#------------------------
#sửa phần tư  
danh_sach_1[4] = "update item"
print(danh_sach_1)
#----------------------------------------------
#xoá phần tử
# pop():xoá ở vị trí cuối cug cua danh sách ->tra về tư   bị xoá 
del_item = danh_sach_1.pop()
print(f"{del_item} da dươc coa khoi danh sach {danh_sach_1}")
#pop(): index xoa ở vị trí index -> tra về phần từ bị xáo 
del_item_1 = danh_sach_1.pop(-1)
print(f"{del_item} da dươc coa khoi danh sach {danh_sach_1}")
#remove(value)xoá phàn tư có value trung khớp có nhu=iều phần tử giống ->xoá ở trái 
# NOTE:
del_item_2 = danh_sach_1.remove(-1)
print(danh_sach_1)
#clear(): xáo hết danh sách 
#print (danh_sach_1.clear())
#----------------------------------------------------------------------
#sắp xêpas danh sách 
#sort (reverse ): neu ?là false : tảng giàn | ? là true : giảm dần
#NOTE:nếu muốn sắp xếp -> cùng kiểu dữ liệu trong dah sách 
danh_sach_2 = ["a","m","A","X","-"]
danh_sach_2.sort(reverse=True)
print(danh_sach_2)
danh_sach_2.sort(reverse=False)
print(danh_sach_2)