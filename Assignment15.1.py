Square = lambda No : No * No


def main():
    Data = [13,12,8,10,11,20]
    
    print("Data is: " , Data)

    MData = list(map(Square, Data))
    print("Data after map is:", MData)
    
if __name__ == "__main__":
    main()