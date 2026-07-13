import threading

Count = 0
lock = threading.Lock()

def Increment():
    global Count

    for i in range(100):
        lock.acquire()
        Count = Count + 1
        lock.release()

def main():
    t1 = threading.Thread(target=Increment)
    t2 = threading.Thread(target=Increment)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Final Counter =", Count)

if __name__ == "__main__":
    main()