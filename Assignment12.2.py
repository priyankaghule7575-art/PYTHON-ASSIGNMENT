def areaofcircle(red):
    PI = 3.14
    print("area of circle is:", PI*red*red)
    

def main():
    red = int(input("Enter the radius of circle:"))

    areaofcircle(red)

if __name__ == "__main__":
    main()