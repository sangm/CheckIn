from models import Student

def transfer_students(raw_students):
    return map(lambda x: Student(username=x.username, givenname=x.givenname, lastname=x.lastname, email=x.email), raw_students)