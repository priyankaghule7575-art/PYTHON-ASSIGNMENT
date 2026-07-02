def binary(no):
    binary_no = ""

    while no > 0:
        a = no % 2
        binary_no= str(a) + binary_no
        no = no // 2

    print("Binary Equivalent:", binary_no)


def main():
    no = int(input("Enter a number: "))
    binary(no)


if __name__ == "__main__":
    main()