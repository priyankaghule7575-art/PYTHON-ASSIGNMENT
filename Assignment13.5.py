def reverse(num):
    rev = 0
    while(num>0):
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    print("reverse number is:",rev)

def main():
    No = int(input("Enter the Number:"))

    reverse(No)


if __name__ == "__main__":
    main()
