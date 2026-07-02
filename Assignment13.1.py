def cheakfunc(ch):
    ch = ch.lower()
    
    if ch=='a' or ch=='e' or ch == 'i' or ch=='o' or ch=='u':
        print("It is Vowel")
    else:
        print("It is consonent")
        
        
def main():
    ch = input("Enter the character:")

    cheakfunc(ch)


if __name__ == "__main__":
    main()
