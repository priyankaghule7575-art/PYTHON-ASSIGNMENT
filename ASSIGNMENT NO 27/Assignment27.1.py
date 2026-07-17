class BookStore:
    NoofBook = 0

    def __init__(self , Name , Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoofBook +=1

    def Display(self):
        print(self.Name , "by",self.Author +".","No of Books",BookStore.NoofBook)

obj1 = BookStore("Linux System Programming" , "Robot Love")
obj1.Display()


obj2 = BookStore("C Programming" , "Dennis Ritche")
obj2.Display()

