def Even(num):
    
    for i in range(1 , num+1):
        
        if i % 2== 0:
            print(i)
    

def main():
    No = int(input("Enter the Number:"))

    Even(No)


if __name__ == "__main__":
    main()
