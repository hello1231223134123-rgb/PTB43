import math
#ham rut gon phan so 

def rut_gon_phanso(tu:int, mau:int):
    #tim ucln de chia ch tu va mau
    ucln = math.gcd(tu, mau)
    tu_moi = tu //ucln #chia lay so nguyen 

    mau_moi = mau//ucln
    return tu_moi, tu_moi
# goi lai han de chay
if __name__ == "__main__":
    print(rut_gon_phanso(6,21))