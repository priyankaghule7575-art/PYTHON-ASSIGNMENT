import threading

def CheakPrime(No):
    if No<2:
        return False
    for i in range(2,No):
        if No% i==0:
            return False
    return True

def Prime(Data):
    print("prime numbers are:")
    for no in Data:
        if CheakPrime(no):
            print(no , " ")
    print()

def NonPrime(Data):
    print("Non prime numbers are:")
    for no in Data:
        if not CheakPrime(no):
            print(no, " ")
    print()




def main():
    Size = int(input("Enter the Number of element"))
    Data=[]
    
    for i in range(Size):
        value=int(input())
        Data.append(value)
    print("Input list is:",Data)

    t1 = threading.Thread(target=Prime , args=(Data,))
    t2 = threading.Thread(target=NonPrime , args=(Data,))

    t1.start()
    t1.join()
    t2.start()
    t2.join()






if __name__ == "__main__":
    main()