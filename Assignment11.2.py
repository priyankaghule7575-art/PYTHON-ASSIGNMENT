def Countdigit(num):
    count=0
    while(num>0):
        num = num//10
        count = count +1
    print("Number of digit is:",count)
        
        
def main():
    No = int(input("Enter the Number:"))

    Countdigit(No)


if __name__ == "__main__":
    main()
