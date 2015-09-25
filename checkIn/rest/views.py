from serializers import StudentSerializer
from rest_framework import viewsets
from models import Student

class StudentViewSet(viewsets.ModelViewSet):
    """
    API Endpoint for list of students
    """
    queryset = Student.objects.all().order_by('username')
    serializer_class = StudentSerializer
