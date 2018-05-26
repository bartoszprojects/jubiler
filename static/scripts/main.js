var app = angular.module('app', ['ngAnimate', 'ui.router', 'ngSanitize']);

app.config(function ($stateProvider, $urlRouterProvider) {
    $urlRouterProvider.otherwise('/home');
    $stateProvider
        .state('home', {
            url: '/home',
            templateUrl: 'home.html'
        })
        .state('services', {
            url: '/services',
            templateUrl: 'services.html',
            controller: 'servicesController'
        })
        .state('about', {
            url: '/about',
            templateUrl: 'about.html',
            controller: 'aboutController'
        })
        .state('products', {
            url: '/products',
            templateUrl: 'products.html',
            controller: 'productsController'
        })
        // .state('products.products_category', {
        //     url: '/products_category/:categoryId',
        //     templateUrl: 'products_category.html',
        //     controller: 'productsCategoryController'
        // })
        // .state('products.products_category.image', {
        //     url: '/image/:imageId',
        //     templateUrl: 'image.html',
        //     controller: 'productsCategoryController'
        // })
        .state('products.product_detail',{
            url: '/:Id',
            templateUrl: 'product.html',
            controller: 'productController'
        })
});

app.service('getDataService', ['$http', function ($http) {
    this.jsonData = function () {
        return {
            'mini_slides_ind':
                $http.get('/slides/mini_slides_ind'),
            'mini_slides_engraving':
                $http.get('/slides/mini_slides_engraving'),
            'mini_slides_repair':
                $http.get('/slides/mini_slides_repair'),
            'main_slider':
                $http.get('/slides/main_slider'),
            'about_informations':
                $http.get('/slides/about_informations'),
            'products':
                $http.get('/products/all'),
            'mini_products':
                $http.get('/products/mini_products'),
            'products_category':
                $http.get('/products/products_category'),
            'product_detail':
                $http.get('/products/product_detail'),
            'services':
                $http.get('/slides/services')
        }
    };
    this.getproduct = function(product_id) {
        return $http.get('/products/product_detail', {pk:product_id})
    }
}]);

app.controller('mainSliderController', function ($scope, getDataService, $rootScope) {

    console.log('from mainSliderController');
    getDataService.jsonData().main_slider.then(ready_data);

    function ready_data(response) {
        if (response.data && response.data[0]) {
            $scope.text = response.data[0].text;
            $scope.baner = response.data[0].baner;
        }
    }
});

app.controller('aboutController', function ($scope, getDataService, $sce) {

    console.log('from about_informations');
    getDataService.jsonData().about_informations.then(ready_data);

    function ready_data(response) {
        $scope.snippet = response.data[0].content;
        $scope.deliberatelyTrustDangerousSnippet = function () {
            return $sce.trustAsHtml($scope.snippet);
        };
    }
});

app.controller('servicesController', function ($scope, getDataService, $sce) {
    getDataService.jsonData().services.then(ready_data);

    function ready_data(response) {
        $scope.services = response.data;
        $scope.snippet = response.data[0].content;

        $scope.deliberatelyTrustDangerousSnippet = function () {
            return $sce.trustAsHtml($scope.snippet);
        };

        console.log('services ', $scope.services[0]);
        console.log('title ', $scope.services[0].title);
        console.log('title ', $scope.services[0].images);

    }
});
app.controller('productController', function ($scope, getDataService, $stateParams) {

    console.log('AAAAAAAAAAAAAAAAAAAAAAAAAAA', $stateParams.Id);
    getDataService.getproduct($stateParams.Id).then(ready_data_detail);

    function ready_data_detail(response) {
        $scope.product = response.data;
    }

});
app.controller('productsController', function ($scope, getDataService, $stateParams) {
    console.log('prodoctsController');



    getDataService.jsonData().products.then(ready_data);


    var element = document.getElementById("active_products");
    element.classList.add("active_all_products");

    function ready_data(response) {
        $scope.products = response.data;
        console.log('products: ', response.data);
        $scope.loadingImage = '../static/images/loading.gif';
        console.log('$scope.products')
    }
});

app.controller('productsCategoryController', function ($scope, getDataService, $stateParams) {
    getDataService.jsonData().products_category.then(ready_data);

    var element = document.getElementById("active_products");
    element.classList.remove("active_all_products");

    function ready_data(response) {
        $scope.categories = response.data;
        $scope.single_category = response.data[$stateParams.categoryId];
        $scope.single_image = response.data[$stateParams.categoryId].category[$stateParams.imageId];
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




app.directive('slider', function () {
        return {
            restrict: 'EA',
            scope: {
                data: '=ngModel'
            },
            replace: true,
            templateUrl: 'slider.html',
            controller: function ($scope, $interval) {

                $scope.currentPosition = 0;
                $scope.image = $scope.data[$scope.currentPosition].image;

                $scope.nextSlide = function () {
                    if ($scope.currentPosition < $scope.data.length - 1) {
                        $scope.currentPosition += 1;

                        $scope.image = $scope.data[$scope.currentPosition].image;

                    } else {
                        $scope.currentPosition = 0;
                        $scope.image = $scope.data[$scope.currentPosition].image;
                    }
                };
                $scope.previousSlide = function () {
                    if ($scope.currentPosition > 0) {
                        $scope.currentPosition -= 1;
                        $scope.image = $scope.data[$scope.currentPosition].image;
                    } else {
                        $scope.currentPosition = $scope.data.length - 1;
                        $scope.image = $scope.data[$scope.currentPosition].image;
                    }
                };


            }
        }
    }
);


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


function directiveSliderFunction() {
    window.onscroll = function () {
        myFunction()
    };

    var header = document.getElementById("myHeader");
    var sticky = header.offsetTop;

    parentwidth = $(".slide_content").width();

    function myFunction() {
        if (window.pageYOffset >= sticky) {
            header.classList.add("sticky");
            $(".child").toggleClass("fixed").width(parentwidth);

        } else {
            header.classList.remove("sticky");
            header.classList.remove("fixed");
        }

    }
}

app.directive('minislider', function () {
    return {
        restrict: 'EA',
        scope: {
            data: '=ngModel'
        },
        replace: true,
        templateUrl: 'mini_slider.html',
        link: directiveSliderFunction
    }
});

app.directive('mainslider', function () {
    return {
        restrict: 'EA',
        scope: {
            data: '=ngModel'
        },
        replace: true,
        templateUrl: 'main_slider.html',
        link: directiveSliderFunction,
        controller: 'mainSliderController'
    }
});


