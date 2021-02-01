class com:
    def __init__(self,e,f):
        self.e = e
        self.f = f
        self.x = complex(e,f)
    def display(self):
        print("The complex number: ",self.x)
    def conj(self):
        print("The conjugate of",self.x,": ",self.x.conjugate())
    def modulus(self):
        print("The modulus of",self.x,": ",abs(self.x))
    def add(self):
        print("The addition of",self.x,"with",2 * self.x,": ",self.x + (2 * self.x))
    def sub(self):
        print("The difference between",self.x,"and",3 * self.x,": ",self.x - (2 * self.x))
    def mult(self):
        print("The product of",self.x,"and",4 * self.x,": ",self.x * (4 * self.x))
    def div(self):
        print("The output of",self.x,"/",5 * self.x,": ",self.x / (5 * self.x))

print("\n\tComplex Numbers and its basic operations\n")
c = int(input("Enter the real part of the complex number: "))
d = int(input("Enter the imaginary part of the complex number: "))
comp = com(c,d)
comp.display()
comp.conj()
comp.add()
comp.sub()
comp.mult()
comp.div()
