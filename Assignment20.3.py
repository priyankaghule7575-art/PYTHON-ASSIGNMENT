import threading

def EvenList(Data):
    sum =0

    print("Even Numbers are:")
    for no in Data:
        if no % 2==0:
            print(no)
            sum = sum + no
    print("Sum of number is:", sum)

def OddList(Data):
    print("Odd Numbers are:")
    sum =0
    for no in Data:
        if no % 2!=0:
            print(no)
            sum = sum +no
    print("Sum of all odd number is:",sum)


def main():
    Size = int(input("Enter the number of element:"))
    Data =[]
    print("Elements are:")
    for i in range(Size):
        value = int(input())
        Data.append(value)


    t1 = threading.Thread(target=EvenList , args=(Data,))
    t2 = threading.Thread(target=OddList , args=(Data,))

    t1.start()
    t1.join()
    t2.start()
    t2.join()

if __name__ == "__main__":
    main()