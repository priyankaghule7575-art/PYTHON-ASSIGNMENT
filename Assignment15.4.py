from functools import reduce

Addition = lambda No1, No2: No1 + No2

def main():
    Data = [10, 20, 30, 40, 50]

    print("Input data is :", Data)

    Result = reduce(Addition, Data)

    print("Addition is :", Result)

if __name__ == "__main__":
    main()
