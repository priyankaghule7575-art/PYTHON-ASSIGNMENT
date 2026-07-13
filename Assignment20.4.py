import threading

def Small(str):
    count =0
    for ch in str:
        if ch.islower():
            count=count+1
    print("Lower case letter is:",count)
    print("TID is:",threading.get_ident())
    print("Thread name is:",threading.current_thread().name)


def Capital(str):
    count =0
    for ch in str:
        if ch.isupper():
            count=count+1
    print("upper case letter is:",count)
    print("TID is:",threading.get_ident())
    print("Thread name  is:",threading.current_thread().name)



def Digits(str):
    count =0
    for ch in str:
        if ch.isdigit():
            count=count+1
    print("number of digit is:",count)
    print("TID is:",threading.get_ident())
    print("Thread name  is:",threading.current_thread().name)

def main():
    value = input("Enter the string:")

    t1 = threading.Thread(target=Small , args=(value,), name="Small")
    t2 = threading.Thread(target=Capital , args=(value,), name="capital")
    t3= threading.Thread(target=Digits , args=(value,), name="Digits")

    t1.start()
    t1.join()
    t2.start()
    t2.join()
    t3.start()
    t3.join()


    print("Exist from main")





if __name__ =="__main__":
    main()