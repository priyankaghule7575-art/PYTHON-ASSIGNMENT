maximum = lambda no1 , no2 : no1 if(no1>no2) else no2

def main():
    value1 = int(input("Enter the first number:"))
    value2 = int(input("Enter the second number"))

    Ret = maximum(value1 , value2)

    print("Maximum number is:", Ret)

    


if __name__ == "__main__":
    main()