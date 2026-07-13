from functools import reduce

GreaterEqual = lambda no: no >= 70 and no <=90

Increment = lambda no :no+10

Product = lambda no1, no2 :no1 * no2





def main():
    Data = []
    Size = int(input("Enter the no of element:"))
    for i in range(Size):
        value = int(input())
        Data.append(value)
    print("input list is:",Data)

    Fdata = list(filter(GreaterEqual,Data))
    print("Data after filter is:",Fdata)       

    Mdata = list(map(Increment , Fdata))
    print("Data after Map is :",Mdata)
    
    Rdata = reduce(Product , Mdata)
    print("Data after reduce is:",Rdata)

if __name__ =="__main__":
    main()