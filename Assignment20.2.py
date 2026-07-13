import threading

def EvenFactor(No):
    Sum =0
    print("Even Thread:",threading.get_ident())
    for i in range(2, No, 2):
        print(i)
        Sum = Sum + i
    print("Summation of all even number is:",Sum)

def Oddfactor(No):
    Sum = 0
    print("Odd Thread:",threading.get_ident())
    
    for i in range(1, No, 2):
        print(i)
        Sum = Sum + i
    print("summation of all odd number is:",Sum)

def main():
    print("Main Thread:",threading.get_ident())
    t1 = threading.Thread(target=EvenFactor , args=(20,))
    t2 = threading.Thread(target=Oddfactor , args=(21,))

    t1.start()
    t1.join()
    t2.start()
    t2.join()

    print("Exist from main")

if __name__ == "__main__":
    main()