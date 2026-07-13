def MaxNum(Data):
    Max = Data[0]
    for no in Data:
        if no > Max:

            Max=no


    return Max



def main():
    NoElement =int(input("Enter the number of element:"))
    Data=[]
    print("Elements are:")

    for i in range(NoElement):
        value = int(input())
        Data.append(value)
    
    Result=MaxNum(Data)

    print("Maximum Number is:",Result)





if __name__ =="__main__":
    main()