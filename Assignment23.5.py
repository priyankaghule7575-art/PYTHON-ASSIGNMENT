import multiprocessing
import os
import time

def FactNum(No):
    print(" PID is :", os.getpid())

    
    Fact =1
    for i in range(1, No+1 ):
        
        Fact = Fact*i
    print("Input Number is" , No)
    print("Factorial is:", Fact)

    return Fact

def main():

    Data = [10, 15, 20 ,25]
    Result = []

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(FactNum, Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()
    

    print("Factorial of  Number is:", Result)
    

    print(f"Time required : {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()