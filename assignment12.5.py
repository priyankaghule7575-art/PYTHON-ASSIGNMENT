def Grade(num):

    if num>=75:
        print("Distinction")
    elif num>=60 :
        print("first Class")

    elif num>=50:
        print("Second class")
    
    elif num<50:
        print("fail")



def main():
    num = int(input("Enter a marks: "))
    Grade(num)


if __name__ == "__main__":
    main()