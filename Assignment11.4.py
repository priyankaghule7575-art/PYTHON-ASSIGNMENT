def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    return rev


def main():
    
    number = int(input("Enter a number: "))
    Ans= reverse_number(number)
    print("Reverse number is:",Ans)

if __name__ == "__main__":
    main()
