from django.db import models


class Student(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    givenname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __unicode__(self):
        return "%s(%s, %s)" % (self.username, self.givenname, self.lastname)


class Course(models.Model):
    course_name = models.CharField(max_length=15)

    def __unicode__(self):
        return "%s:%s" % ("Course Name", self.course_name)


class StudentCourse(models.Model):
    student = models.ForeignKey(Student)
    course = models.ForeignKey(Course)

    def __unicode__(self):
        return "%s: %s" % (self.student.username, self.course.course_name)

    @property
    def username(self):
        return self.student.username

    @property
    def course_name(self):
        return self.course.course_name


class RawStudentData(models.Model):
    """
    Student data generated from https://www.mockaroo.com/
    """
    username = models.CharField(max_length=50, primary_key=True)
    givenname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    course1 = models.CharField(max_length=5, null=True)
    course2 = models.CharField(max_length=5, null=True)
    course3 = models.CharField(max_length=5, null=True)

    def __unicode__(self):
        return "%s, %s, %s, %s: (%s, %s, %s)" % (self.username, self.givenname, self.lastname, self.email,
                                                 self.course1, self.course2, self.co)

