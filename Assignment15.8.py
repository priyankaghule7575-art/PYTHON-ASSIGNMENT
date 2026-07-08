CheakData = lambda No : (No % 3==0 ) and (No % 5==0)

def main():
    Data = [20, 12, 35, 32 , 90, 45]

    print("Input data is :", Data)

    FData = list(filter(CheakData, Data))

    print("Number is divisible by 3 and 5 :", FData)

if __name__ == "__main__":
    main()