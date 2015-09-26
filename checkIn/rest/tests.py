from django.test import TestCase
from models import RawStudentData, Student, StudentCourse, Course
from utils import transfer_students, transfer_courses, transfer_students_courses


class TransferTest(TestCase):
    def setUp(self):
        RawStudentData.objects.create(username="sangm", givenname="sang", lastname="mercado", email="hi@sangm.io",
                                      course1="CS100", course2="CS200")
        RawStudentData.objects.create(username="gloriaj", givenname="gloria", lastname="jauregui",
                                      email="gloria@jauregui.io", course1="CS200", course2="CS500")

        Student.objects.create(username="sangm", givenname="sang", lastname="mercado", email="hi@sangm.io"),
        Student.objects.create(username="gloriaj", givenname="gloria", lastname="jauregui", email="gloria@jauregui.io")

        Course.objects.create(course_name="CS100")
        Course.objects.create(course_name="CS200")
        Course.objects.create(course_name="CS500")

        StudentCourse.objects.create(student=Student.objects.get(username="sangm"),
                                     course=Course.objects.get(course_name="CS100"))
        StudentCourse.objects.create(student=Student.objects.get(username="sangm"),
                                     course=Course.objects.get(course_name="CS200"))
        StudentCourse.objects.create(student=Student.objects.get(username="gloriaj"),
                                     course=Course.objects.get(course_name="CS200"))
        StudentCourse.objects.create(student=Student.objects.get(username="gloriaj"),
                                     course=Course.objects.get(course_name="CS500"))

    def test_transfer_students_info(self):
        students = transfer_students(RawStudentData)

        self.assertItemsEqual(Student.objects.all(), students)

    def test_transfer_courses(self):
        expected_courses = [u"CS100", u"CS200", u"CS500"]
        courses = transfer_courses(RawStudentData)
        course_names = map(lambda x: x.course_name, courses)

        self.assertItemsEqual(expected_courses, course_names)

    def test_transfer_student_courses(self):
        expected_records = [
            (u'sangm', u'CS100'),
            (u'sangm', u'CS200'),
            (u'gloriaj', u'CS200'),
            (u'gloriaj', u'CS500')
        ]

        records = transfer_students_courses(Student, Course, RawStudentData)
        record_names = map(lambda x: (x.student.username, x.course.course_name), records)

        self.assertItemsEqual(expected_records, record_names)
