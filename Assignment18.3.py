def MinNum(Data):
    Min = Data[0]
    for no in Data:
        if no < Min:

            Min=no


    return Min



def main():
    NoElement =int(input("Enter the number of element:"))
    Data=[]
    print("Elements are:")

    for i in range(NoElement):
        value = int(input())
        Data.append(value)
    
    Result=MinNum(Data)

    print("Minimum Number is:",Result)





if __name__ =="__main__":
    main()