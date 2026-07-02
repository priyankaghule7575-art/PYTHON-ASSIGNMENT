def ChkGreater(No1, No2):

    if(No1 > No2):
        print("No1 is greater")
    else:
        print("No2 is greater")
     

def main():
     a = int(input("Enter the first Number: "))
     b = int(input("Enter Second Number :"))
 
     ChkGreater( a , b)

if __name__ == "__main__":
     main()
