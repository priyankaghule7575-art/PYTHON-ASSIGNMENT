def Cube(No1):

    Ans = No1 **3

    return Ans     

def main():

    a = int(input("Enter the Number: "))
    Ret = Cube(a)

    print("Cube  of Number is:" , Ret)

if __name__ == "__main__":
    main()
