import multiprocessing
import os
import time

def Factorial(No):
    print("Process is running with PID : ",os.getpid())
    
    Fact = 1

    for i in range(1,No+1):
        Fact= Fact* i

    return Fact

def main():
    Data = [10 , 15 , 20 ,25]
    Result = []

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool() 

    Result = pobj.map(Factorial,Data)

    pobj.close()
    pobj.join()
    
    end_time = time.perf_counter()

    print("Factorial of Number is : ")
    print(Result)

    print(f"Time required : {end_time-start_time:.4f} seconds")

if __name__ == "__main__":
    main()
