def Factorial(num):
    fact = 1
    for i in range(1 , num+1):
     
        fact = fact * i
    print("factorial of number is" ,num ,"is:", fact)
    

def main():
    No = int(input("Enter the Number:"))

    Factorial(No)


if __name__ == "__main__":
    main()
