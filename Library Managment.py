# This is library management system
# the user can borrow, return and donate the books to library
import sys

# Making the class Library
class Library:


    def __init__(self, list_of_book):
        # List_of_books stores the books list
        self.availablebook = list_of_book

    def display_books(self):
        print('------ This library has following books ---')
        # this will print the list of the books
        for books in self.availablebook:
            print(books)

    def lend_book(self, Borrowed_book):
        # Borrowed_book takes input from the student class and will work with self.availablebook
        if Borrowed_book in self.availablebook:
            print('Library has this particular book and can be borrowed')
            self.availablebook.remove(Borrowed_book)
        else:
            print("Sorry, This time the book is already borrowed by someone else")

    def add_book(self, returned_book):
        # returned_book takes input from the student class and will work with self.availablebook
        # you can remove the print statement if you want to
        print('Thank you for returning the book')
        self.availablebook.append(returned_book)

    def donate_book(self, book_donation):
        # book_donation takes input from the student class and will work with self.availablebook
        # you can remove the print statement if you want to
        print('Thank you for donating the book to the library')
        self.availablebook.append(book_donation)


class Student:

    def request_book(self):
        print('Enter the name of the book you want to borrow :')
        self.book = input()
        return self.book

    def return_book(self):
        print('Enter the name of the book you want to return')
        self.book = input()
        return self.book

    def d_book(self):
        print('Enter the name of the book you want to donate')
        self.book = input()
        return self.book

def main():
    # initialising the parameters
    lib = Library(['Mechanics of Materials', 'Engineering Mechanics', 'Physics Fundamentals', 'Introduction to Automotive Electronics'])
    student = Student()

    k = True
    while k == True:
        # Menu for the Library. You can change accordingly
        print("""Welcome to the library. Here is the menu of the library
                ========================================================
                1. Display all the books available in the library
                2. Rent a book
                3. Return a book
                4. Donate a book to library
                5. Exit """)

        option = int(input('Enter the number :'))
        # options are based on the above menu

        if option == 1:
            lib.display_books()
        elif option == 2:
            lib.lend_book(student.request_book())    # when calling this generally the thing under the parenthesis is run first and then outside parenthsis
        elif option == 3:
            lib.add_book(student.return_book())
        elif option == 4:
            lib.donate_book(student.d_book())
        else:
            sys.exit()  # exit the system completely

main()

