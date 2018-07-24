var app = angular.module('app', ['ngAnimate', 'ui.router', 'ui.bootstrap', 'ngSanitize']);

app.run(function($rootScope, $uibModal) {
    $rootScope.openModalImage = function(imageSrc) {
        $uibModal.open({
            templateUrl: "image_modal.html",
            resolve: {
                imageSrcToUse: function () {
                    return imageSrc;
                }
            },
            controller: ["$scope", "imageSrcToUse", function($scope, imageSrcToUse) {
                $scope.ImageSrc = imageSrcToUse;
            }]
        });
    };
});

app.config(function ($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

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
        .state('terms', {
            url: '/terms',
            templateUrl: 'terms.html'
        })
        .state('products', {
            url: '/products',
            templateUrl: 'products.html',
            controller: 'productsController'
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
        .state('products.product_details', {
            url: '/product_details/:productId',
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
            'services':
                $http.get('/slides/services')
        }
    };
    this.getproduct = function (product_id) {
        return $http.get('/products/product_details/' + product_id, {pk: product_id})
    }
}]);

app.controller('mainSliderController', function ($scope, getDataService, $rootScope) {
    getDataService.jsonData().main_slider.then(ready_data);

    function ready_data(response) {
        if (response.data && response.data[0]) {
            $scope.text = response.data[0].text;
            $scope.baner = response.data[0].baner;
        }
    }
});

app.controller('aboutController', function ($scope, getDataService, $sce) {
    getDataService.jsonData().about_informations.then(ready_data);

    function ready_data(response) {
        $scope.snippet = response.data[0].content;
        $scope.deliberatelyTrustDangerousSnippet = function () {
            return $sce.trustAsHtml($scope.snippet);
        };
    }
});

app.controller('servicesController', function ($scope, getDataService, $sce, $http) {
    getDataService.jsonData().services.then(ready_data);

    function ready_data(response) {
        $scope.services = response.data;

        $scope.MakeTrustedDjangoCKEDITORContent = function (snippet_number) {
            return $sce.trustAsHtml(response.data[snippet_number].content);
        };
    }

    $scope.sendMail = function () {
        $http({
            method: 'POST',
            url: '/slides/services',
            data: {data: 'title'}
        })
    };

});

app.controller('productController', function ($scope, getDataService, $stateParams) {
    getDataService.getproduct($stateParams.productId).then(ready_data);

    function ready_data(response) {
        $scope.product = response.data;
        $scope.image_in_product = $scope.product.to_product.image.large[0];
        $scope.large_image = $scope.product.to_product.image.large;
        $scope.small_image = $scope.product.to_product.image.small;
        $scope.clickMe = function (number) {
            $("#image_animation").hide().fadeIn();
            $scope.image_in_product = $scope.large_image[number]
        }
    }
});

app.controller('productsController', function ($scope, getDataService, $stateParams) {
    getDataService.jsonData().products.then(ready_data);
    var element = document.getElementById("active_products");
    element.classList.add("active_all_products");

    function ready_data(response) {
        $scope.products = response.data;
        $scope.loadingImage = '../static/images/loading.gif';
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

        $scope.large_image = $scope.single_image.to_product.image.large;
        $scope.small_image = $scope.single_image.to_product.image.small;

        $scope.image_in_product = $scope.single_image.to_product.image.large[0];

        $scope.clickMe = function (number) {
            $("#image_animation").hide().fadeIn();
            $scope.image_in_product = $scope.single_image.to_product.image.large[number]
        }
    }
});

app.controller('miniproducstController', function ($scope, getDataService) {
    getDataService.jsonData().mini_products.then(ready_data);

    function ready_data(response) {
        $scope.products = response.data;
    }
});

app.controller('contactController', function ($scope, $http) {
    $scope.form_data = {
        'image': null
    };
    $scope.isChecked = false;
    $scope.checkTerms = function () {
        if ($scope.isChecked === false) {
            $(".check_terms").css({"background": "#7c8ea4"});
            $(".submit_button").css({"display": "block"});
            $scope.isChecked = true;
        }
        else {
            $(".check_terms").css({"background": "white"});
            $(".submit_button").css({"display": "none"});
            $scope.isChecked = false;
        }

    };
    $scope.sendMail = function () {

        var url = '/slides/contact';
        var data = {
            name: $scope.name,
            email: $scope.email,
            phone_number: $scope.phone_number,
            message: $scope.message
        };
        if ($scope.form_data.image != null) {
            data.image = $scope.form_data.image;
        }
        $http.post(url, data).then(success);
        $(".contact_circle").css({'display': "block"});

        function success() {
            $(".contact_circle").css({'display': "none"});
            $("form :input[type='text'],input[type='email'],input[type='number'], textarea").val('');
          }
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
                $scope.image = $scope.data[$scope.currentPosition].image_thumbnail;

                $scope.nextSlide = function () {
                    if ($scope.currentPosition < $scope.data.length - 1) {
                        $scope.currentPosition += 1;

                        $scope.image = $scope.data[$scope.currentPosition].image_thumbnail;

                    } else {
                        $scope.currentPosition = 0;
                        $scope.image = $scope.data[$scope.currentPosition].image_thumbnail;
                    }
                };
                $scope.previousSlide = function () {
                    if ($scope.currentPosition > 0) {
                        $scope.currentPosition -= 1;
                        $scope.image = $scope.data[$scope.currentPosition].image_thumbnail;
                    } else {
                        $scope.currentPosition = $scope.data.length - 1;
                        $scope.image = $scope.data[$scope.currentPosition].image_thumbnail;
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
