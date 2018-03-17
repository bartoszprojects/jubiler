const app = angular.module('app', ['ngAnimate', 'ui.router']);

app.config(function ($stateProvider, $urlRouterProvider) {

    $urlRouterProvider.otherwise('/');

    $stateProvider
        .state('main_page', {
            url: '/',
            templateUrl: 'index.html'
        })
        .state('services', {
            url: '/services',
            templateUrl: 'services.html'
        })
        .state('products', {
            url: '/products',
            templateUrl: 'products.html',
        })



});















app.service('getDataService', ['$http', function ($http) {
    this.jsonData = function () {
        return {
            'mini_slides_ind' : $http.get('http://127.0.0.1:8000/slides/mini_slides_ind'),
            'products' : $http.get('http://127.0.0.1:8000/products/all'),
         }}
}]);

app.controller('mainSliderController', function($scope, getDataService, $http) {
    $http.get('http://127.0.0.1:8000/slides/main_slider').then(ready_data);

    function ready_data(response) {
        $scope.text = response.data[0].text;
        $scope.baner = response.data[0].baner;
    }
});


app.controller('MiniSliderIndividual', function ($scope, getDataService, $timeout) {

    getDataService.jsonData().mini_slides_ind.then(ready_data);
    $scope.temp = 1;

    function ready_data(response) {
        $scope.slajd = response.data[0].image;

        $scope.nextSlide = function () {
            next(response)
        };
        $scope.previousSlide = function () {
            previous(response)
        };

        $scope.returnSlide = function (slideNumber) {
            return response.data[slideNumber].image;
        }
    }
    function next(response) {
        if ($scope.temp <= response.data.length - 1) {
            $scope.slajd = $scope.returnSlide($scope.temp);
            $scope.temp += 1;

        }
        if ($scope.temp === response.data.length + 1) {
            $scope.temp = 1;
            $scope.slajd = $scope.returnSlide($scope.temp);
        }
    }
    function previous(response) {
        if ($scope.temp > 1) {
            $scope.temp -= 1;
            $scope.slajd = $scope.returnSlide($scope.temp - 1);
        }
    }
});

app.controller('productsController', function ($scope, getDataService) {
    getDataService.jsonData().products.then(ready_data);

    function ready_data(response) {
        $scope.products = response.data
    }
});

app.controller('miniproducstController', function ($scope, getDataService, $http) {
    $http.get('http://127.0.0.1:8000/products/mini_products').then(ready_data);
    function ready_data(response) {
        $scope.products = response.data;

    }
});


