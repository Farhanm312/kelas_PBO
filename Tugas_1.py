class student:
    def __init__(self,n,a,j):
        self.full_name = n
        self.age = a
        self.job = j
    def get_age(self):
        return self.age
    def job(self):
        return self.job
    
f = student("farhan",19,"Mahasiswa")

print(f.full_name)
print(f.get_age())
print(f.job)