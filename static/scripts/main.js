const app = angular.module('app', ['ngAnimate']);

app.service('getDataService', ['$http', function ($http) {
    this.jsonData = function () {
        return $http.get('/data/mini_slides_ind/')
    }
}]);

app.controller('MiniSliderIndividual', function ($scope, getDataService, $timeout) {

    getDataService.jsonData().then(ready_data);
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




