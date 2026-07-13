def DisplayPattern(No):
    for i in range(No):
        print("* " * No)

def main():
    Value = int(input("Enter the number: "))
    DisplayPattern(Value)

if __name__ == "__main__":
    main()