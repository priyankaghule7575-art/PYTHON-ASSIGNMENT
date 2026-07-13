Mult = lambda No1 , No2: No1*No2

def main():

    value1 =int(input("Enter the Number:"))
    value2 = int(input("Enter the second Number:"))

    Ret = Mult(value1 , value2)
    print("Multiplication  of Number is:", Ret)

if __name__ == "__main__":
    main()