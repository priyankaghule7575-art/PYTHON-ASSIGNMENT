def Fact(No):
    fact = 1
    for i in range(1 ,  No+1):
        
        fact = fact*i

    return fact

def main():
    Value = int(input("Enter the number: "))
    Result=Fact(Value)
    print("Factorial of number is:", Result)

if __name__ == "__main__":
    main()