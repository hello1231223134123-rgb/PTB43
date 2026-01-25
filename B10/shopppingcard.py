cart = []
funncs = ["1 thêm vào giỏ",
           "2.chỉnh sửa món hàng",
           "3.xoá mon hàng(theo index )",
            "4. sắp xếp theo tên ",
            "5.thoát chương trình "
        ]
#bắt đầu chương trình 
while True: 
    #in danh sách tính năng
    for value in funncs:
        print (value) 

    # chon 1 chức năng 
    choice  = int(input("chọn 1 chức năng:"))
    # nếu không chọn đúng ->báo nỗi 
    while(choice > 5 or choice < 0 ):
        choice = int(input("chọn 1 chức năng (0->5):"))
        #func 5 
        if choice == 5 :
            print("Bye!")
            break
        #FUNC 0:
        if  choice == 0:
             if len(cart)==0:
                print("giỏ hàng rong")
                continue 
             for i in range (len(cart)):
                print(f"{i}: {cart}")
        #funnc 1 :
        elif choice == 1:
            pass
        # func 2:
        elif choice == 2:
            pass
        # func 3:
        elif choice == 3:
            pass
        # func 4:
        elif choice == 4:
            pass