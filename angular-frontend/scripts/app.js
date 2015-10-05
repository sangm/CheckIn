'use strict';

angular
    .module('tutoringLoginApp', [
        'ngResource',
        'ngRoute',
        'ngAnimate',
        'ui.bootstrap'
    ])

    .config(function ($routeProvider, $httpProvider) {
        $routeProvider
            .when('/', {
                templateUrl: 'views/students.html',
                controller: 'StudentCtrl'
            })
            .otherwise({
                redirectTo: '/'
            });

        $httpProvider.defaults.headers.common = {
            'Authorization': 'Token 34d8f7901120fc135ba114896f5d77274385d30f',
        }
    });
