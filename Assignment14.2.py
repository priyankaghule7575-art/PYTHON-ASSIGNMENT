CubeNum = lambda no: (no*no*no)

def main():
    value = int(input("Enter the number:"))
    Ret = CubeNum(value)

    print("Cube of number is:",Ret)


if __name__ == "__main__":
    main()
