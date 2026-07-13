from functools import reduce

def CheakPrime(no):
    if no < 2:
        return False
    for i in range(2 , no):
        if no%i==0:
            return False
        
    return True

multby2= lambda no : no*2

Maximum = lambda no1, no2 :no1  if no1>no2 else no2

def main():
    Data = []
    Size = int(input("Enter the no of element:"))
    for i in range(Size):
        value = int(input())
        Data.append(value)
    print("input list is:",Data)

    Fdata = list(filter(CheakPrime ,Data))
    print("Data after filter is:",Fdata)       

    Mdata = list(map(multby2 , Fdata))
    print("Data after Map is :",Mdata)
    
    Rdata = reduce(Maximum , Mdata)
    print("Data after reduce is:",Rdata)

if __name__ =="__main__":
    main()