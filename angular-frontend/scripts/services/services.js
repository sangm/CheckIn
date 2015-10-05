'use strict';

var apiUrl = 'http://localhost:8000/v1'

angular
    .module('tutoringLoginApp')
    .factory('StudentFactory', ['$resource', function($resource) {
        return $resource(apiUrl + '/:action/:param', {
            action : '@action',
            param: '@param'
        });
    }])

    .service('StudentListService', function() {
        var studentList = [];

        this.addStudent = function(student) {
            console.debug(studentList.indexOf(student));
            studentList.push(student);
        };

        this.removeStudent = function(index) {
            studentList.splice(index, 1);
        };

        this.getStudents = function() {
            return studentList;
        }
    });

