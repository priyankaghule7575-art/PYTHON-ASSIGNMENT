IsDivisible = lambda No: No % 5 == 0

def main():
    Value = int(input("Enter a number: "))

    Ret = IsDivisible(Value)

    print(Ret)

if __name__ == "__main__":
    main()
