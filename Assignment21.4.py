import threading


def SumofElement(Data):
    sum = 0
    for i in Data:
        sum = sum + i
    print("sum of numbers from list is",sum)

def ProductofElement(Data):
    product = 1
    for i in Data:
        product = product * i
    print("Product of element in list is:", product)



def main():
    Size = int(input("Enter the Number of element"))
    Data=[]
    
    for i in range(Size):
        value=int(input())
        Data.append(value)
    print("Input list is:",Data)

    t1 = threading.Thread(target=SumofElement , args=(Data,))
    t2 = threading.Thread(target=ProductofElement, args=(Data,))

    t1.start()
    t1.join()
    t2.start()
    t2.join()






if __name__ == "__main__":
    main()