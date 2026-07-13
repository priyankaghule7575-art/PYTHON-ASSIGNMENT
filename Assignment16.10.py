def DisplayLength(Name):
    return len(Name)

def main():
    Name = input("Enter your name: ")

    Result = DisplayLength(Name)

    print("Length of name is:", Result)

if __name__ == "__main__":
    main()