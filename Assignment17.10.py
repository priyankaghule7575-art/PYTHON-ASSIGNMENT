def Display(No):
    digit = 0
    sum=0
    while No > 0:
        digit = digit+1
        sum = sum+digit
        No =No//10
    print("Number of digit is:",sum)

        

def main():
    Value = int(input("Enter the number: "))
    Display(Value)

if __name__ == "__main__":
    main()