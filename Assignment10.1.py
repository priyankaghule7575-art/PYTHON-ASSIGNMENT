def Multtable(Num1):
    for i in range(1, 11):

        print(Num1 ,"X", i, "=" ,Num1* i)



def main():
    Num=int(input("Enter the Number: " ))
    Multtable(Num)

   #............... print("Multiplication Table is :", Ret)

if __name__ == "__main__":
    main()
