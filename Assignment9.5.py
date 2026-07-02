def Cheak(No1):

    if (No1 % 3==0 and No1 % 5==0):
        print("Number is Divisible by 3 and 5")
    else:
        print("Number is not Divisible by 3 and 5")

         

def main():

    a = int(input("Enter the Number: "))
    Cheak(a)

    

if __name__ == "__main__":
    main()
