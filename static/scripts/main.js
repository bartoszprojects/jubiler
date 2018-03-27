const app = angular.module('app', ['ngAnimate', 'ui.router']);

app.config(function ($stateProvider, $urlRouterProvider) {
    $urlRouterProvider.otherwise('/home');
    $stateProvider
        .state('home', {
            url: '/home',
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
            'mini_slides_ind':
                $http.get('http://127.0.0.1:8000/slides/mini_slides_ind'),
            'mini_slides_engraving':
                $http.get('http://127.0.0.1:8000/slides/mini_slides_engraving'),
            'mini_slides_repair':
                $http.get('http://127.0.0.1:8000/slides/mini_slides_repair'),
            'main_slider':
                $http.get('http://127.0.0.1:8000/slides/main_slider'),
            'products':
                $http.get('http://127.0.0.1:8000/products/all'),
            'mini_products':
                $http.get('http://127.0.0.1:8000/products/mini_products'),
            'products_category':
                $http.get('http://127.0.0.1:8000/products/products_category')
        }
    }
}]);

app.controller('mainSliderController', function ($scope, getDataService) {
    console.log('from mainSliderController');
    getDataService.jsonData().main_slider.then(ready_data);

    function ready_data(response) {
        if (response.data && response.data[0]) {
            $scope.text = response.data[0].text;
            $scope.baner = response.data[0].baner;
        }
    }
});

app.controller('productsController', function ($scope, getDataService) {
    console.log('prodoctsController');
    getDataService.jsonData().products.then(ready_data);

    function ready_data(response) {
        $scope.products = response.data;
        console.log('products: ', response.data)
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
        console.log('mini products ', response.data)
    }
});

app.controller('productsCategoryController', function ($scope, getDataService, $stateParams) {
    getDataService.jsonData().products_category.then(ready_data);

    function ready_data(response) {
        $scope.categories = response.data;
        $scope.single_category = response.data[$stateParams.categoryId];

        if (response.data[$stateParams.categoryId].category) {
            $scope.single_image = response.data[$stateParams.categoryId].category[$stateParams.imageId];
        }

        $scope.bartek = 'hehehe';
        console.log('categories', $scope.categories)
    }
});

app.controller('MiniSlider', function ($scope, getDataService) {
    getDataService.jsonData().mini_slides_ind.then(function (response) {
        $scope.mini_slides_ind = response.data;
    });
    getDataService.jsonData().mini_slides_engraving.then(function (response) {
        $scope.mini_slides_engraving = response.data;
    });
    getDataService.jsonData().mini_slides_repair.then(function (response) {
        $scope.mini_slides_repair = response.data;
    });
});

app.directive('slider', function () {
    return {
        restrict: 'EA',
        scope: {
            data: '=ngModel'
        },
        replace: true,
        templateUrl: 'slider.html'

        ,
        controller: function ($scope) {
            $scope.currentPosition = 0;
            $scope.image = $scope.data[$scope.currentPosition].image;

            $scope.nextSlide = function () {
                if ($scope.currentPosition < $scope.data.length - 1) {
                    $scope.currentPosition += 1;
                    $scope.image = $scope.data[$scope.currentPosition].image;
                } else {
                    $scope.currentPosition = 0;
                }
            };
            $scope.previousSlide = function () {
                if ($scope.currentPosition > 0) {
                    $scope.currentPosition -= 1;
                } else {
                    $scope.currentPosition = $scope.data.length - 1;
                }
            };

            $scope.$watch('currentPosition', function (newVal) {
                $scope.image = $scope.data[$scope.currentPosition].image;
                $scope.apply();
            })
        }
    }
});
