class Member:
    def __init__(self, member_id, name,borrowed_books=None):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = borrowed_books if borrowed_books else []
    def __str__(self):
        return f"Member(ID: {self.member_id}, Name: '{self.name}', Borrowed Books: {self.borrowed_books})"
    

class Student(Member):
    def __init__(self, member_id, name, student_id, borrowed_books):
        super().__init__(member_id, name,borrowed_books)
        self.student_id = student_id
        self.borrowing_limit=3

    def __str__(self):
        return f"Student(ID: {self.member_id}, Name: '{self.name}', Student ID: '{self.student_id}', Borrowed Books: {self.borrowed_books})"

        
           
        


class Faculty(Member):
    def __init__(self, member_id, name, faculty_id, borrowed_books):
        super().__init__(member_id, name,borrowed_books)
        self.faculty_id = faculty_id
        self.borrowing_limit=5

    def __str__(self):
        return f"Faculty(ID: {self.member_id}, Name: '{self.name}', Faculty ID: '{self.faculty_id}')"

# student1 = Student("M01", "Prava", "ST01")
# faculty1 = Faculty("M02", "Ram", "FC01")

# print(student1)
# print(faculty1)

# print(student1.borrowing_limit)
# print(faculty1.borrowing_limit)