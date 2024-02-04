class library:
    def __init__(self):
        self.books= ['The Psychology of Money', '12 Rules for Life', 'The Kite Runner', 'Encyclopedia of the World', 'The Oxford Dictionary']
        print('''=====Welcome to the Central Library of Chandrapur=====
Please select what task do you want to do in the library :
1: Display Available Books
2: Request a Book
3: Submit a Book
4: Exit the library\n''')

    def DisplayAvailableBooks(self):
        print("The available books are as follows:")
        print("  * ",end='')
        a="\n  * ".join(self.books)
        print(a)

    def Issue(self, Book):
        if Book in self.books:
            print("You have been issued the book. Please keep it safe and return it within 15 days..Happy reading!")
            self.books.remove(Book)
        else : print("Sorry! the book is not available in the library. Please check for the availability after some time")
     
    def Deposit(self, Book):
        print("The Book has been submitted to the library. Have a nice day")
        self.books.append(Book)
        
        
class student:
    def __init__(self, name):
        self.name= name
        print(f'''Hello {name}''')
        
    def Display(self):
        library.DisplayAvailableBooks(self)
    def Request(self):
        Book=input("Which book do you want to request from the library? : ")

        library.Issue(Book)
    def Submit(self):
        Book= input("Which book do you want to submit? : ")


lib= library()

stu= student("Shubham")
while True:
    choice= int(input("What's your choice : "))
    if choice==1: lib.DisplayAvailableBooks()
    elif choice==2 : 
        Book=input("Which book do you want to request from the library? : ")
        lib.Issue(Book)
        
    elif choice==3 : 
        Book=input("Which book do you want to submit to the library? : ")
        lib.Deposit(Book)
        
    elif choice==4 : break
    else: print("invalid choice. Please try again...")
