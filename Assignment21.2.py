import threading

def Maximum(Data):
    max = Data[0]
    for i in Data:
        if i>max:
            max = i
    print("max element is", max)        

def Minimum(Data):
    min = Data[0]
    for i in Data:
        if i<min:
            min = i
    print("max element is", min)        




def main():
    Size = int(input("Enter the Number of element"))
    Data=[]
    
    for i in range(Size):
        value=int(input())
        Data.append(value)
    print("Input list is:",Data)

    t1 = threading.Thread(target=Maximum , args=(Data,))
    t2 = threading.Thread(target=Minimum, args=(Data,))

    t1.start()
    t1.join()
    t2.start()
    t2.join()






if __name__ == "__main__":
    main()