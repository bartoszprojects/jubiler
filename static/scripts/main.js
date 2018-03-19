
const app = angular.module('app', ['ngAnimate', 'ui.router']);

app.config(function ($stateProvider, $urlRouterProvider) {

    $urlRouterProvider.otherwise('/');

    $stateProvider
        .state('home', {
            url: '/',
            templateUrl: 'home.html'
        })
        .state('services', {
            url: '/services',
            templateUrl: 'services.html'
        })
        .state('products', {
            url: '/products',
            templateUrl: 'products.html'
        })
        .state('products.products_category', {
                url: '/products_category/:categoryId',
                templateUrl: 'products_category.html',
                controller: 'productsCategoryController'
            })
        .state('products.products_category.image', {
            url: '/image/:imageId',
            templateUrl: 'image.html',
            controller: 'productsCategoryController'
        })
});

app.service('getDataService', ['$http', function ($http) {
    this.jsonData = function () {
        return {
            'mini_slides_ind' :
                $http.get('http://127.0.0.1:8000/slides/mini_slides_ind'),
            'mini_slides_engraving' :
                $http.get('http://127.0.0.1:8000/slides/mini_slides_engraving'),
            'mini_slides_repair' :
                $http.get('http://127.0.0.1:8000/slides/mini_slides_repair'),
            'main_slider' :
                $http.get('http://127.0.0.1:8000/slides/main_slider'),
            'products' :
                $http.get('http://127.0.0.1:8000/products/all'),
            'mini_products' :
                $http.get('http://127.0.0.1:8000/products/mini_products'),
            'products_category' :
                $http.get('http://127.0.0.1:8000/products/products_category')
         }}
}]);

app.controller('mainSliderController', function($scope, getDataService, $http) {
    console.log('from mainSliderController');
    getDataService.jsonData().main_slider.then(ready_data);
    function ready_data(response) {
        $scope.text = response.data[0].text;
        $scope.baner = response.data[0].baner;
    }
});

app.controller('MiniSliderIndividual', function ($scope, getDataService, $q) {
    console.log('from MiniSliderIndividual');
    $scope.temp = 1;
    $scope.myNumber = 0;
    var promises = [
        getDataService.jsonData().mini_slides_ind,
        getDataService.jsonData().mini_slides_repair,
        getDataService.jsonData().mini_slides_engraving
    ];
    $q.all(promises).then(ready_data);

    function ready_data(response) {
        $scope.slajd = response[$scope.myNumber].data[0].image;

        $scope.nextSlide = function (number) {
            next(response, number)
        };
        $scope.previousSlide = function (number) {
            previous(response, number)
        };
    }
    function next(response, number) {
        if ($scope.temp <= response[number].data.length - 1) {
            $scope.slajd = response[number].data[$scope.temp].image;
            $scope.temp += 1;

        }
        if ($scope.temp === response[number].data.length + 1) {
            $scope.temp = 1;
            $scope.slajd = response[number].data[$scope.temp].image;
        }
    }
    function previous(response, number) {
        if ($scope.temp > 1) {
            $scope.temp -= 1;
            $scope.slajd = response[number].data[$scope.temp - 1].image;
        }
    }
});

app.controller('productsController', function ($scope, getDataService) {
    console.log('prodoctsController');
    getDataService.jsonData().products.then(ready_data);
    function ready_data(response) {
        $scope.products = response.data;
    }

    $scope.galleryFilter = function (x) {
        $scope.xFilter = x
    }
});

app.controller('miniproducstController', function ($scope, getDataService) {
    console.log('miniproductsController');
    getDataService.jsonData().mini_products.then(ready_data);
    function ready_data(response) {
        $scope.products = response.data;

    }
});

app.controller('productsCategoryController', function ($scope, getDataService, $stateParams) {
    getDataService.jsonData().products_category.then(ready_data);
    function ready_data(response) {
        $scope.categories = response.data;
        $scope.single_category = response.data[$stateParams.categoryId];
        $scope.single_image = response.data[$stateParams.categoryId].category[$stateParams.imageId];
        $scope.bartek = 'hehehe'
    }

});

