CheckEven = lambda No: (No % 2 == 0)

def main():
    Data = [16, 18, 80, 10, 12, 26]

    print("Input List :", Data)

    FData = list(filter(CheckEven, Data))

    Count = len(FData)

    print("Count of even numbers :", Count)

if __name__ == "__main__":
    main()