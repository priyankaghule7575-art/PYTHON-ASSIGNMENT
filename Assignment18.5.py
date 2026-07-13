import MarvellousNum
def ListPrime(Arr):
    sum = 0
    for i in Arr:
        if MarvellousNum.ChkPrime(i):
            sum = sum + i
    return sum






def main():
    NoElement=int(input("Enter the number of Element:"))
    Data=[]
    print("Enter the Element:")
    for i in range(NoElement):

        value = int(input())
        Data.append(value)

    
    Ans = ListPrime(Data )
    print("Addition of prime number is:",Ans)



if __name__ == "__main__":
    main()