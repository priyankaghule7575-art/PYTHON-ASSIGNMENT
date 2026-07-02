def Square(No1):

    Ans = No1 * No1

    return Ans     

def main():

    a = int(input("Enter the Number: "))
    Ret = Square(a)

    print("Square of Number is:" , Ret)

if __name__ == "__main__":
    main()
