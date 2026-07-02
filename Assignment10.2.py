def NaturalSum(num):
    sum=0
    for i in range(1 , num+1):
        
        sum = sum + i
    print("Sum of  natural number" ,num ,"is:", sum)
    

def main():
    No = int(input("Enter the Number:"))

    NaturalSum(No)


if __name__ == "__main__":
    main()
