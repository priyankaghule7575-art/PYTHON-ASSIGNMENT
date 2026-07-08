CheckLength = lambda Str: len(Str) > 5

def main():
    Data = ["Priyanka", "viren", "Deepak", "Gauri", "Manisha", "Nidhi"]

    print("Input List :", Data)

    FData = list(filter(CheckLength, Data))

    print("Strings having length greater than 5 :", FData)

if __name__ == "__main__":
    main()