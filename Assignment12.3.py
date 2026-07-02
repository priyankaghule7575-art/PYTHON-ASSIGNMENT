def perfect(no):
    total = 0

    for i in range(1, no):
        if no % i == 0:
            total += i

    if total == no:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")


def main():
    no= int(input("Enter a number: "))
    perfect(no)


if __name__ == "__main__":
    main()