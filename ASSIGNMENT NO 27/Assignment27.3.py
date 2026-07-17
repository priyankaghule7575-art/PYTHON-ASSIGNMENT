class Number:
    def __init__(self , value):
        self.value = value

    def ChkPrime(self):
        if self.value <=1:
            return False
        for i in range(2, int(self.value ** 0.5)+1):
            if self.value % i ==0:
                return False
        return True

    def ChkPerfect(self):
        sum =0
        for i in range(1 , self.value):
            if self.value % i ==0:
                sum = sum + i
        if sum == self.value:
            return True
        else:
            return False
        
    def Factor(self):
        print("Factor of",self.value,"are:")
        for i in range(1 , self.value +1):
            if self.value % i==0:
                print(i , end=" ")

        print()

    def sumFactor(self):
        sum = 0
        for i in range(1,self.value+1):
            if self.value % i==0:
                sum = sum+i
        return sum

def main():
    obj1 = Number(6)
    obj2 =Number(13)

    print("----Object1------")
    print("Prime Number is:",obj1.ChkPrime())
    print("Perfect Number is:",obj1.ChkPerfect())
    obj1.Factor()
    print("Sum of factor is:",obj1.sumFactor())

    print("----Object2-----")
    print("Prime Number is:",obj1.ChkPrime())
    print("Perfect Number is:",obj2.ChkPerfect())
    obj1.Factor()
    print("Sum of factor is:",obj2.sumFactor())

if __name__ == "__main__":
    main()

