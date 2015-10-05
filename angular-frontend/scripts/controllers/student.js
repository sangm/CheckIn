angular
    .module('tutoringLoginApp')
    .controller('StudentCtrl', function($scope, StudentFactory, StudentListService) {
        $scope.students = StudentListService.getStudents(); 
    
        $scope.removeStudent = function(index) {
            StudentListService.removeStudent(index);
        };
    });
