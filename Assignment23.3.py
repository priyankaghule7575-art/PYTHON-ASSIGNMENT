import multiprocessing
import os
import time

def EvenNo(No):
    print(" PID is :", os.getpid())

    
    count =0
    for i in range(2, No+1 ,2):
        
        count = count+1

    return count

def main():

    Data = [1000000, 2000000, 3000000 ,4000000, 5000000]
    Result = []

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(EvenNo, Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()
    

    print("Even Numbers are:", Result)
    

    print(f"Time required : {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()