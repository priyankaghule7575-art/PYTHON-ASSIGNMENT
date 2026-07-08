Mult = lambda no1 , no2 : no1 * no2

def main():
    value1 = int(input("Enter the first number:"))
    value2 = int(input("Enter the second number:"))

    Ret = Mult(value1 , value2)

    print("Multiplication of  number is:", Ret)

    


if __name__ == "__main__":
    main()