def Prime(num):
    count = 0
    for i in range(1 , num+1):
        
        if num % i== 0:
            count = count + 1
            
    if count == 2:
        print(num , "is prime number")
    else:
        print(num , "is not prime")
    

def main():
    No = int(input("Enter the Number:"))

    Prime(No)


if __name__ == "__main__":
    main()
