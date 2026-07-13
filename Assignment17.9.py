def Display(No):
    digit = 0
    while No > 0:
        digit = digit+1
        No =No//10
    print("Number of digit is:",digit)

        

def main():
    Value = int(input("Enter the number: "))
    Display(Value)

if __name__ == "__main__":
    main()