import Arithmatic

def main():
    No1 = int(input("Enter first Number:"))
    No2 = int(input("Enter Second Number:"))

    Result1 = Arithmatic.Addition(No1 , No2)
    print("Addition of Number is:",Result1)

    
    Result2 = Arithmatic.Subtraction(No1 , No2)
    print("Subtraction of Number is:",Result2)

    
    Result3 = Arithmatic.Multiplication(No1 , No2)
    print("Multiplication of Number is:",Result3)

    
    Result4= Arithmatic.Division(No1 , No2)
    print("Division of Number is:",Result4)

if __name__ =="__main__":
    main()