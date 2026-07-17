class Arithmatic:


    def __init__(self):
        self.value1 =0
        self.value2 =0

    def Accept(self):
        self.value1 =int(input("Enter the First Number:"))
        self.value2 =int(input("Enter the Second Number:"))

    def Addition(self):
        return self.value1+self.value2

    def Subtraction(self):
        return self.value1 - self.value2
    
    def Multiplication(self):
        return self.value1 * self.value2
    
    def Division(self):
        if self.value2==0:
            return "Division by zero not possible"
        else:
            return self.value1 / self.value2

    

obj1 = Arithmatic()
obj1.Accept()

print("Addition is:" , obj1.Addition())
print("Subtraction is is:" , obj1.Subtraction())
print("Multiplication  is:" , obj1.Multiplication())
print("Division is:" , obj1.Division())

print("----------------------------------------")

obj2= Arithmatic()
obj2.Accept()

print("Addition is:" , obj1.Addition())
print("Subtraction is is:" , obj1.Subtraction())
print("Multiplication  is:" , obj1.Multiplication())
print("Division is:" , obj1.Division())


