def AddFact(No):
    sum = 0
    for i in range(1 ,No+1):
        if No % i == 0:
            sum = sum +i
    return sum

def main():
    Value = int(input("Enter the number: "))
    Result = AddFact(Value)
    print("Addition of factorial no is:",Result)

if __name__ == "__main__":
    main()