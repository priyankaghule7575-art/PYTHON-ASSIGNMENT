def calculate(no1,no2):

    print("Addition of number is:",no1+no2)
    print("Subtraction of number is:",no1-no2)
    print("multiplication of number is:",no1*no2)
    print("Division of number is:", no1/no2)
    
        
        
def main():
    no1 = int(input("Enter the first number:"))
    no2 = int(input("Enter the second number:"))
    
    calculate(no1,no2)


if __name__ == "__main__":
    main()
