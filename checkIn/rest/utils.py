from models import RawStudentData, Student, Course, StudentCourse


def transfer_students(raw_students_data):
    records = raw_students_data.objects.all()
    return map(lambda x: Student(username=x.username, givenname=x.givenname, lastname=x.lastname, email=x.email), records)


def transfer_courses(raw_students_data):
    records = raw_students_data.objects.all()
    # these functions implemented in FP style.. because I wanna!
    # list comprehension, set(list) will improve performance greatly
    courses = map(lambda x: (x.course1, x.course2, x.course3), records)
    flat_courses = reduce(lambda x, y: x+y, map(list, courses))
    unique_courses = filter(lambda x: x is not None, set(flat_courses))
    return map(lambda x: Course(course_name=x), unique_courses)


def create_student_course(student, courses, course_name):
    try:
        course = courses.objects.get(course_name=course_name)
        return StudentCourse(student=student, course=course)
    except Course.DoesNotExist:
        return None


def transfer_students_courses(students, courses, raw_student_data):
    student_courses = []
    raw_records = raw_student_data.objects.all()

    for record in raw_records:
        student = students.objects.get(username=record.username)
        student_courses.append(create_student_course(student, courses, record.course1))
        student_courses.append(create_student_course(student, courses, record.course2))
        student_courses.append(create_student_course(student, courses, record.course3))

    return filter(lambda x: x is not None, student_courses)


def save_students():
    students = transfer_students(RawStudentData)
    save_models(students)


def save_courses():
    courses = transfer_courses(RawStudentData)
    save_models(courses)


def save_student_courses():
    student_courses = transfer_students_courses(Student, Course, RawStudentData)

    save_models(student_courses)


def save_models(models):
    for model in models:
        model.save()

