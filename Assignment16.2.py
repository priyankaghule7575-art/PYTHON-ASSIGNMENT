def ChkNum(No):
    if (No % 2 == 0):
        print("Number is Even")
    else:
        print("number is odd")


def main():
    value1 = int(input("Enter the Number:"))

    ChkNum(value1)

if __name__ == "__main__":
    main()