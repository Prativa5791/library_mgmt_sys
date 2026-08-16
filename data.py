# from book import Book
# from member import Student, Faculty
# from library import Library

# lib = Library()

# # create objects
# book1 = Book("9780134685991", "Effective Python", "Brett Slatkin", 5, 5)
# book2 = Book("9781492056355", "Fluent Python", "Luciano Ramalho", 3, 2)

# student1 = Student("S001", "Alice Johnson", [])
# student2 = Student("S002", "Bob Smith", [])

# faculty1 = Faculty("F001", "Dr. Carol Lee", [])
# faculty2 = Faculty("F002", "Prof. David Kim", [])

# # add to library
# lib.books.extend([book1, book2])
# lib.members.extend([student1, student2, faculty1, faculty2])

# # save to CSV
# lib.add_book("123", "Effective Python", "Brett Slatkin", 5)
# lib.add_book("456", "Fluent Python", "Luciano Ramalho", 3)
# lib.register_member("S001", "Alice Johnson", "student")
# lib.register_member("S002", "Bob Smith", "student")
# lib.register_member("F001", "Dr. Carol Lee", "faculty")
# lib.register_member("F002", "Prof. David Kim", "faculty")

# lib.issue_book("123", "S001")
from library import Library

lib = Library()

# Add books
lib.add_book("123", "Effective Python", "Brett Slatkin", 5)
lib.add_book("456", "Fluent Python", "Luciano Ramalho", 3)

# Register members
lib.register_member("S001", "Alice Johnson", "student")
lib.register_member("S002", "Bob Smith", "student")
lib.register_member("F001", "Dr. Carol Lee", "faculty")
lib.register_member("F002", "Prof. David Kim", "faculty")

# Test issuing a book
lib.issue_book("123", "S001")