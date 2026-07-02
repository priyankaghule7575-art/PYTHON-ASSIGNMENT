def Sumdigit(num):
    sum = 0
    while(num>0):
        DIGIT = num % 10
        sum = sum + DIGIT
        num = num //10
    print(sum)


def main():
    No = int(input("Enter the Number:"))

    Sumdigit(No)


if __name__ == "__main__":
    main()
