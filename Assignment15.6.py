from functools import reduce

MinimumNum= lambda No1, No2 : No1 if No1<No2 else No2

def main():
    Data = [10, 20, 30, 40, 50]

    print("Input data is :", Data)

    Result = reduce(MinimumNum, Data)

    print("Minimun Number is :", Result)

if __name__ == "__main__":
    main()