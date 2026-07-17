import multiprocessing
import os
import time

def CntPrime(No):
    print("Process is running with PID :", os.getpid())

    Count = 0

    for i in range(2, No + 1):

        Prime = True

        for k in range(2, int(i ** 0.5) + 1):
            if i % k == 0:
                Prime = False
                break

        if Prime:
            Count = Count + 1

    return Count

def main():

    Data = [1000, 2000, 3000, 4000]
    Result = []

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(CntPrime, Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print("Prime count between 1 to N is :")
    print(Result)

    print(f"Time required : {end_time-start_time:.4f} seconds")

if __name__ == "__main__":
    main()