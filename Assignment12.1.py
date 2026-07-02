def area(len , width):

    print("area of rectangle is:", len*width)
    

def main():
    len = int(input("Enter the length of Number:"))

    width = int(input("Enter the width of rectangle"))
    area(len , width)

if __name__ == "__main__":
    main()