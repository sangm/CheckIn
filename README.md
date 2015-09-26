I generated mock data from website: https://www.mockaroo.com

sqlite3 import command:
`.read FILENAME`

set up sqlite3 driver in intellij

# DJANGO Examples
+ To run shell `python manage.py shell`
+ To get all raw student data object `a = RawStudentData.object.all()`

# Setup MySQL Environment
+ Under checkIn/sql_setup run `./insert_data.sh` that will create the database and insert mock data
+ To populate data from raw data do the following commands under checkIn directory
+ create a superuser by running `python manage.py createsuperuser`
+ `python manage.py makemigrations`
+ `python manage.py migrate`
+ `python manage.py shell`
+ `from rest.utils import *`
+ `save_students()`
+ `save_courses()`
+ `save_student_courses()`

# Obtaining Token
+ I use httpie to send POST request, it's trivial to convert the following command to curl if you do not want to 
install it
+ `http POST http://localhost:8000/api-token-auth/ username=sangm password=DBPassword`
