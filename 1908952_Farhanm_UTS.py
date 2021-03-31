print("~~~~~~~~~~~~~~~~~~~~~~")
print("Nama : Farhan Maulana")
print("NIM  : 1908952")
print("~~~~~~~~UTS PBO~~~~~~~")
print(" ")

class Sinobi:
    
    def __init__(self,N,K,A,D,P):
        
        self.Nama = N
        self.Kelamin = K
        self.Alamat = A
        self.Desa = D
        self.Pangkat = P
    
    def get_Kelamin(self):
        return self.Kelamin
    
    def get_Alamat(self):
        return self.Alamat
    
    def get_Desa(self):
        return self.Desa
    
    def get_Pangkat(self):
        return self.Pangkat
    
f = Sinobi("Naruto Uzumaki","laki-Laki","Jln.Rasengan no.01 block c","Konoha","Sinobi Chunnin")

print("Biodata :")
print(" ")
print(f.Nama)
print(f.get_Kelamin())
print(f.get_Alamat())
print(f.get_Desa())
print(f.get_Pangkat())