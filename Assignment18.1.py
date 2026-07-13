def Addition(Data):
    sum = 0
    for i in Data:
        sum = sum + i

    return sum



def main():
    NoElement =int(input("Enter the number of element:"))
    Data=[]
    print("Elements are:")

    for i in range(NoElement):
        value = int(input())
        Data.append(value)
    
    Result=Addition(Data)

    print("Addition of all element is:",Result)





if __name__ =="__main__":
    main()