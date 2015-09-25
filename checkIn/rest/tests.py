from django.test import TestCase
from models import RawStudentData, Student
from utils import transfer_students

# Create your tests here.
class TransferTest(TestCase):
    def test_smoke_test(self):
        raw_students = [
            RawStudentData(username="sangm", givenname="sang", lastname="mercado", email="hi@sangm.io",
                           course1="CS100"),
            RawStudentData(username="gloriaj", givenname="gloira", lastname="jauregui", email="gloria@jauregui.io",
                           course1="CS200", course2="CS100")
        ]
        expected_students = [
            Student(username="sangm", givenname="sang", lastname="mercado", email="hi@sangm.io"),
            Student(username="gloriaj", givenname="gloira", lastname="jauregui", email="gloria@jauregui.io")
        ]
        students = transfer_students(raw_students)

        self.assertEqual(expected_students, students)
