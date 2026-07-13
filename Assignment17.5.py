def ChkPrime(No):
    

    count =0
    for i in range (1 , No+1):
        if No%i==0:
            count = count+1

    if count ==2:
        print("It is a Prime Number")    
    else:
        print("It is not Prime Number")
    
 

def main():
    Value = int(input("Enter the number: "))
    ChkPrime(Value)

if __name__ == "__main__":
    main()