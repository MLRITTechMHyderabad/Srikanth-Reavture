class A:
    def __init__(self, a):
        self.a=a 
    def display(self):
        print("A:",self.a)
class B(A):
    def __init__(self,a,b):
        super().__init__(a)
        self.b=b 
    def display_b(self):
        print(self.b,self.a)


class C(B):
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c=c 
    def display_c(self):
        print(self.c,self.a,self.b)
class D(B):
    def __init__(self,a,b,d):
        super().__init__(a,b)
        self.d=d 
    def display_d(self):
        print(self.d,self.a,self.b)
class E(D,C):
    def __init(self,a,b,c,d,e):
        super().__init__(a,b,c,d)
        self.e=e 
    def display_e(self):
        print(self.e,self.a,self.b,self.c,self.d)

e = E(1, 2, 3, 4, 5)
e.display_e()