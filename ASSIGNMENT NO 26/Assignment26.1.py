class Demo:
    
    value =20
    def __init__(self , A , B):
        self.no1 = A
        self.no2 =B

    def Fun(self):
        print("Inside Fun()")
        print("Value of no1 :", self.no1)
        print("Value of no2 :",self.no2)

    def Gun(self):
        print("Inside Fun()")
        print("Value of no1 :", self.no1)
        print("Value of no2 :",self.no2)

obj1 = Demo(11,21)
obj2 = Demo(51 , 101)
obj1.Fun()
obj2.Fun()
obj1.Gun()
obj2.Gun()
