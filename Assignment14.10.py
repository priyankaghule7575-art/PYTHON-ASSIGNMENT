MaxNum = lambda No1 , No2 ,No3: No1 if (No1 > No2 and No1 > No3) else (No2 if No2 > No3 else No3)

def main():
    value1 = int(input("Enter the first number:"))
    value2 = int(input("Enter the second number:"))
    value3 = int(input("Enter Third number"))

    Ret = MaxNum(value1 , value2 , value3)

    print("Minimum number is:", Ret)

    


if __name__ == "__main__":
    main()