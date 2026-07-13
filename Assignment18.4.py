
def Frequency(Arr , No):
    count = 0
    for i in Arr:
        if i == No:
            count = count+1
    return count
    








def main():
    NoElement=int(input("Enter the number of Element:"))
    Data=[]
    print("Enter the Element:")
    for i in range(NoElement):

        value = int(input())
        Data.append(value)

    Find = int(input("Enter the element to search:"))
    Ans = Frequency(Data , Find)
    print("Frequency is:",Ans)



if __name__ == "__main__":
    main()