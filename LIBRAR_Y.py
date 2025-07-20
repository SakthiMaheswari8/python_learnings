''' '''
class Library:
    def __init__(self, books):
        self.books = list(books)   

    def available_book(self):
        print(f"\n{len(self.books)} books available:")
        for b in self.books:
            print("*", b)
        print()

    def borrow_book(self, book):
        for b in self.books:
            if b.lower() == book.lower():
                self.books.remove(b)
                print("Book issued.\n")
                return
        print("The book is not available.\n")

    def return_book(self, book):
        entry = {book}
        if entry in self.books:
            self.books.append(book)
            print("Book returned\n")
        else:
            print("this book is not available in our library.\n")
        
class Student:
    def request_book(self):
        book = input("Name of the book you want to borrow: ")
        return book

    def return_book(self):
        book = input("Name of the book you want to return: ")
        return book

def main():
    titles = ["C", "C++", "Python", "Java"]
    lib = Library(titles)
    user = Student()
    print("Welcome to ABC Library")
    print("1. List of books\n2. Borrow book\n3. Return book\n4. Exit\n")
    while True:
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Enter a number.\n")
            continue
        if choice == 1:
            lib.available_book()
        elif choice == 2:
            book = user.request_book()
            lib.borrow_book(book)
        elif choice == 3:
            book = user.return_book()
            lib.return_book(book)
        elif choice == 4:
            print("Thank You\n")
            break
        else:
            print("Invalid choice.\n")
if __name__ == "__main__":
    main()
