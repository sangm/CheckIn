'use strict';
angular
    .module('tutoringLoginApp')
    .controller('MainCtrl', function ($scope, StudentFactory, StudentListService) {
        // Represnt each indvidual student attained from services and providers
        $scope.student = {
            courses: [],
            name: '',
            netid: '',
            query: '',
        };

        StudentFactory.query({action:'students'}).$promise.then(function(students) {
            $scope.students = [];
            angular.forEach(students, function(student) {
                $scope.students.push({
                    netid: student.username,
                    name: "".concat(student.givenname,
                                    ' ', student.lastname)
                });
            });
            return $scope.students;
        });

        $scope.getCourses = function(query) {
            query = query.split(' | ');
            $scope.student.name = query[0];
            $scope.student.netid = query[1];
            $scope.student.courses = [];
            $scope.showCourses = true;
            StudentFactory.query({action:'student-courses', username:$scope.student.netid})
                .$promise.then(function(courses) {
                    angular.forEach(courses, function(course) {
                        $scope.student.courses.push(course);
                    });
                    return $scope.student.courses;
                });
        };

        $scope.addStudent = function(student, course) {
            console.log(course);
            student.query = undefined;
            student.courses = undefined;
            student.selectedCourse = course.course_name;
            StudentListService.addStudent(student);
            $scope.student = "";
        };

        $scope.$watch('student.query', function() {
            if (!$scope.student.query)
                $scope.showCourses = false;
        });
    });

