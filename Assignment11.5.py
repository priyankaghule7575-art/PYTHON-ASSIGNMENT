def Palindrom_Number(num):

    original = num
    reverse = 0

    while num > 0:  
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num// 10

        if original == reverse:
            print("Palindrome Number")
        else:
            print("Not a Palindrome Number")


def main():
    num = int(input("Enter a number: "))
    Palindrom_Number(num)


if __name__ == "__main__":
    main()
