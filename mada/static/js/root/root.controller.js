angular.module('numadaApp')
.controller('BaseController', ['$scope',
    '$mdBottomSheet',
    '$mdSidenav',
    'baseService',
    'txnService',
    function ($scope, $mdBottomSheet, $mdSidenav, baseService, txnService) {

    $scope.name = "MADA"
    $scope.minDate = new Date("2016-06-01");

    $scope.init = function (date) {
        $scope.selectedDate = new Date(date);
        $scope.maxDate = new Date(date);

        // updateForDate($scope.selectedDate);
    }

    $scope.$watch(function () {
        return $scope.selectedDate;
    }, function (newVal, oldVal) {
        if (newVal != oldVal) {
            updateForDate(new Date(newVal.getTime() - newVal.getTimezoneOffset()*60000));
        }
    })

    function updateForDate(date) {
        console.log('called');
        $scope.selected_section.dataSource(date).then(function (data) {
            $scope.items = data;
        }, function (response) {
            $scope.items = [];
        });
    };

    $scope.selected_section     = null;
        $scope.selected_tabs = [];
        $scope.sections        = [ ];
        $scope.selectSection   = selectSection;
        $scope.toggleList   = toggleUsersList;

        // Load all registered users

        baseService
                    .loadAllSections()
                    .then( function(sections) {
                        $scope.sections = [].concat(sections);
                        $scope.selectSection(0);
                    });

        /**
         * Hide or Show the 'left' sideNav area
         */
        function toggleUsersList() {
            $mdSidenav('left').toggle();
        }

        /**
         * Select the current avatars
         * @param menuId
         */
        function selectSection (section) {
            $scope.selected_section = angular.isNumber(section) ? $scope.sections[section] : section;
            baseService.loadTabs(section).then(function (tabs) {
                $scope.selected_tabs = tabs;
            });
            updateForDate($scope.selectedDate);
        }

        
}]);