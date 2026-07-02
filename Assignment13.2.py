def factor(num):
    
    print("Factors are:")
    for i in range(1, num+1):
        if num % i ==0:
            print(i)
        
        
def main():
    num = int(input("Enter the Number:"))

    factor(num)


if __name__ == "__main__":
    main()
