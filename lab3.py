class Book:
    def __init__(self):
        self.book_id = ""
        self.book_title = ""
        self.author_id = ""
        self.publisher = ""
        self.year_of_publication = ""

    def add_book(self):
        self.book_id = int(input("Enter book id: "))
        self.book_title = input("Enter book title: ")
        self.author_id = int(input("Enter author id: "))
        self.publisher = input("Enter publisher: ")
        self.year_of_publication = int(input("Enter year of publication: "))

    def display_book(self):
        print("BOOK INFO")
        print("Book id: ", self.book_id)
        print("Book title: ", self.book_title)
        print("Author id: ", self.author_id)
        print("Publisher: ", self.publisher)
        print("Year of publication: ", self.year_of_publication)


class Author:
    def __init__(self):
        self.author_id = ""
        self.author_name = ""
        self.affiliation = ""
        self.country = ""
        self.phone = ""
        self.emailid = ""

    def add_author(self):
        self.author_id = int(input("Enter author id: "))
        self.author_name = input("Enter author name: ")
        self.affiliation = input("Enter affiliation: ")
        self.country = input("Enter country: ")
        self.phone = int(input("Enter phone: "))
        self.emailid = input("Enter emailid: ")

    def display_author(self):
        print("AUTHOR INFO")
        print("Author id: ", self.author_id)
        print("Author name: ", self.author_name)
        print("Affiliation: ", self.affiliation)
        print("Country: ", self.country)
        print("Phone: ", self.phone)
        print("Emailid: ", self.emailid)


class User:
    def __init__(self):
        self.user_id = ""
        self.name = ""
        self.password = ""
        self.address = ""
        self.phone = ""
        self.emailid = ""
        self.books_borrowed = []

    def add_user(self):
        self.user_id = int(input("Enter user id: "))
        self.name = input("Enter name: ")
        self.password = input("Enter password: ")
        self.address = input("Enter address: ")
        self.phone = int(input("Enter phone: "))
        self.emailid = input("Enter emailid: ")

    def borrow_book(self,book_object):
        self.books_borrowed.append(book_object)
        print("Book added to user's borrowed books.")

    def display_user(self):
        print("USER INFO")
        print("User id: ", self.user_id)
        print("Name: ", self.name)
        print("Password: ", self.password)
        print("Address: ", self.address)
        print("Phone: ", self.phone)
        print("Emailid: ", self.emailid)
        print("Books borrowed:")
        if not self.books_borrowed:
            print("No books borrowed.")
        else:
            for book in self.books_borrowed:
                print(book.book_id, book.book_title)




myBooksList = []
myAuthorsList = []
myUsersList = []

while 1:
    print("MAIN MENU")
    print("1. Add Book")
    print("2. Add Author")
    print("3. Add User")
    print("4. Borrow Book")
    print("5.Display info")
    print("6.Exit")
    choice = int(input("Enter your choice: "))

    if choice == 6:
        print("Thank you. You are now exiting...")
        break

    elif choice == 1:
        bk = Book()
        bk.add_book()
        myBooksList.append(bk)
        print("Book added")

    elif choice == 2:
        ath = Author()
        ath.add_author()
        myAuthorsList.append(ath)
        print("Author added")

    elif choice == 3:
        u = User()
        u.add_user()
        myUsersList.append(u)
        print("User added")

    elif choice == 4:
        if not myUsersList:
            print("No users in the list.")

        elif not myBooksList:
            print("No books in the list.")

        else:
            user_id = int(input("Enter user id: "))
            book_id = int(input("Enter book id: "))

            found_user = ""
            found_book = ""

            for user in myUsersList:
                if user.user_id == user_id:
                    found_user = user

            for book in myBooksList:
                if book.book_id == book_id:
                    found_book = book

            if found_user is None:
                print("User not found.")
            elif found_book is None:
                print("Book not found.")
            else:
                found_user.borrow_book(found_book)

    elif choice == 5:
        print("DISPLAY INFO MENU")
        print("1. Display book info")
        print("2. Display author info")
        print("3. Display user info")
        print("4. Display all info")
        print("5. Exit")
        choice2 = int(input("Enter your choice: "))

        if choice2 == 5:
            print("Thank you. You are now exiting...")
            break

        elif choice2 == 1:
            if not myBooksList:
                print("No books in the list.")

            else:
                for book in myBooksList:
                    book.display_book()

        elif choice2 == 2:
            if not myAuthorsList:
                print("No authors in the list.")

            else:
                for author in myAuthorsList:
                    author.display_author()

        elif choice2 == 3:
            if not myUsersList:
                print("No users in the list.")

            else:
                for user in myUsersList:
                    user.display_user()

        elif choice2 == 4:
            print("BOOKS")
            for book in myBooksList:
                book.display_book()

            print ("AUTHORS")
            for author in myAuthorsList:
                author.display_author()

            print("USERS")
            for user in myUsersList:
                user.display_user()

        else:
            print("Invalid choice.")

    else:
        print("Invalid choice.")


