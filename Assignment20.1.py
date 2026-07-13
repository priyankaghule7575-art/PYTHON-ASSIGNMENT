import threading

def Even():
    print("Even Thread:",threading.get_ident())
    for i in range(2, 21, 2):
        print(i)

def Odd():
    print("Odd Thread:",threading.get_ident())
    
    for i in range(1, 20, 2):
        print(i)

def main():
    print("Main Thread:",threading.get_ident())
    t1 = threading.Thread(target=Even)
    t2 = threading.Thread(target=Odd)

    t1.start()
    t1.join()
    t2.start()
    t2.join()

    print("End of main")

if __name__ == "__main__":
    main()