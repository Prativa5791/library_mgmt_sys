import book
from member import Student, Faculty
import csv
class Library:

    def __init__(self):
        self.books = []
        self.fieldnames = ['isbn', 'title', 'author', 'total_copies', 'available_copies']
        with open('data/books.csv', 'w', newline='') as file:
            

            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()

    def add_book(self, isbn, title, author, total_copies):

        # Create Book object
        new_book = book.Book(
            isbn,
            title,
            author,
            total_copies,
            total_copies
            
        )
        self.books.append(new_book)


        with open('data/books.csv', mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writerow({
                'isbn': new_book.isbn,
                'title': new_book.title,        

                'author': new_book.author,
                'total_copies': new_book.total_copies,
                'available_copies': new_book.available_copies


                        })
    def register_member(self, member_id   , name, member_type):
        if member_type == "student":
            new_member = Student(member_id, name,  [])
        elif member_type == "faculty":
            new_member = Faculty(member_id, name, [])
        else:
            raise ValueError("Invalid member type. Must be 'student' or 'faculty'.")
        return new_member
        

        
    
        
        
        
library = Library()

library.add_book(
    101,
    "Python Programming",
    "Guido van Rossum",
    5
)

print(library.books[0])

