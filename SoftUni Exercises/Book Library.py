from datetime import datetime

number_of_inputs = int(input('Number of inputs: '))

class Book:

    # Setting the values for a book
    def __init__(self, title, author, publisher, date, isbn, price):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.date = datetime.strptime(date, '%d.%m.%Y')
        self.isbn = int(isbn)
        self.price = float(price)

class Library:

    # Creating a list to hold Book instances
    books = []

    def __init__(self, name):
        self.name = name

    # function for adding books and printing a msg
    def AddBook(self, book):
        self.books.append(book)
        print(f'{book.title} was added to Library {self.name}')

    # function for viewing books in the given library
    def ViewBooks(self):
        for i in range(0, len(self.books)):
            print(f'Book {i + 1} - {self.books[i].title}, date - {self.books[i].date}')
    
    # Function for printing every unique author and the total price of his books(ordered)
    def AuthorsTotalPrice(self):
        author_total = {}

        # Adding every unique author in a dictionary and summing the price of their books 
        for book in self.books:
            if book.author not in author_total:
                author_total[book.author] = book.price
            else:
                author_total[book.author] += book.price
        
        # Printing the dictionary in sorted by highest value order
        for auth, price in sorted(author_total.items(), key=lambda item: item[1], reverse=True):
            print(f'{auth} -> {price:.2f}')
        
        print('\n---------------------------')
    
    # Function for printing books after a given date(ordered)
    def BookAfterDate(self):
        book_dates = {}

        target_date = datetime.strptime(input('Target date: '), '%d.%m.%Y')
        print()

        # Adding all the books after the target date to a list
        for book in self.books:
            if book.date > target_date:
                book_dates[book.title] = book.date
        
        # Printing the books sorted by date
        for title, date in sorted(book_dates.items(), key=lambda item: item[1]):
            print(f'{title} -> {date.strftime("%d.%m.%Y")}')
        
        print('\n---------------------------')

    
# Creating a Library instance
book_library = Library('Orange')

for i in range(0, number_of_inputs):
    
    # Accepting and converting the user input
    temp_inp = input(f'Book {i+1} - ')
    book_info = temp_inp.split()

    # Creating a book instance and adding it to the library
    new_book = Book(book_info[0], book_info[1], book_info[2], book_info[3], book_info[4], book_info[5])
    book_library.books.append(new_book)

print('\n---------------------------')

# Printing the desired output : )

book_library.AuthorsTotalPrice()

book_library.BookAfterDate()
