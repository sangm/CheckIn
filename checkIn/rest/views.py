from rest_framework.response import Response
from serializers import StudentSerializer, CourseSerializer, StudentCourseSerializer
from rest_framework import viewsets, filters
from models import Student, Course, StudentCourse
import django_filters


class StudentCourseFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(name="student__username")

    class Meta:
        model = StudentCourse
        fields = ['username']


class StudentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API Endpoint for list of students
    """
    queryset = Student.objects.all().order_by('username')
    serializer_class = StudentSerializer
    pagination_class = None


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API Endpoint for list of courses
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = None


class StudentCourseViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API Endpoint for list of student courses
    """
    queryset = StudentCourse.objects.all()
    serializer_class = StudentCourseSerializer
    pagination_class = None
    filter_class = StudentCourseFilter






