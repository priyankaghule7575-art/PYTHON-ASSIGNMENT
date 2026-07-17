import multiprocessing
import os
import time

def SumOdd(No):
    print("PID IS: " , os.getpid())
    Sum =0

    
    for i in range(1, No ,2):
        Sum = Sum + i

    return Sum


def main():
    Data =[1000000 , 2000000 ,3000000 , 4000000 ,5000000]
    Rsult=[]
    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumOdd , Data)
    pobj.close()

    pobj.join()

    end_time = time.perf_counter()

    print("Sum :" , Result)

    
    print(f"Time required : {end_time - start_time:.4f} seconds")


if __name__ == "__main__":
    main()