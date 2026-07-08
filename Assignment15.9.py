from functools import reduce

Product = lambda No1, No2: No1 * No2

def main():
    Data = [5, 55, 23, 15, 40, 32]

    print("Input Data:", Data)

    RData = reduce(Product, Data)

    print("Product of all numbers :", RData)

if __name__ == "__main__":
    main()