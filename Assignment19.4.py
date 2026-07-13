from functools import reduce

CheakEven = lambda no: no % 2== 0 

Square = lambda no :no*no

Addition = lambda no1, no2 :no1 + no2





def main():
    Data = []
    Size = int(input("Enter the no of element:"))
    for i in range(Size):
        value = int(input())
        Data.append(value)
    print("input list is:",Data)

    Fdata = list(filter(CheakEven,Data))
    print("Data after filter is:",Fdata)       

    Mdata = list(map(Square , Fdata))
    print("Data after Map is :",Mdata)
    
    Rdata = reduce(Addition , Mdata)
    print("Data after reduce is:",Rdata)

if __name__ =="__main__":
    main()