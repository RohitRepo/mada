angular.module('numadaApp')
.controller('BaseController', ['$scope',
    '$mdBottomSheet',
    '$mdSidenav',
    'baseService',
    'txnService',
    function ($scope, $mdBottomSheet, $mdSidenav, baseService, txnService) {

    $scope.name = "MADA"
    $scope.minDate = new Date("2016-06-01");
    $scope.selected_section = null;
    $scope.selected_tabs = [];
    $scope.sections = [ ];
    $scope.selectSection = selectSection;
    $scope.toggleList = toggleUsersList;
    $scope.selectedDateStart;
    $scope.selectedDateEnd;
    $scope.showSelectedDateEnd = false;
    $scope.showProgress = false;

    $scope.init = function (date) {
        $scope.selectedDateStart = new Date(date);
        $scope.selectedDateEnd = new Date(date);
        $scope.maxDate = new Date(date);
    }

    baseService
        .loadAllSections()
        .then( function(sections) {
            $scope.sections = [].concat(sections);
            $scope.selectSection(0);
        });

    function toggleUsersList() {
        $mdSidenav('left').toggle();
    }

    $scope.$watch(function () {
        return $scope.selectedDateStart;
    }, function (newVal, oldVal) {
        if (newVal != oldVal) {
            updateData([new Date(newVal.getTime() - newVal.getTimezoneOffset()*60000), $scope.selectedDateEnd]);
        }
    })

    $scope.$watch(function () {
        return $scope.selectedDateEnd;
    }, function (newVal, oldVal) {
        if (newVal != oldVal) {
            updateData([$scope.selectedDateStart, new Date(newVal.getTime() - newVal.getTimezoneOffset()*60000)]);
        }
    })

    function updateData(dates) {
        showProgress();
        $scope.selected_tab.dataSource(dates).then(function (data) {
            $scope.items = data;
            console.log('Got data', data);
            hideProgress();
        }, function (response) {
            hideProgress();
            $scope.items = [];
        });
    };

    var showProgress = function () {
        $scope.showProgress = true;
    };

    var hideProgress = function () {
        $scope.showProgress = false;
    };

    function selectSection (section) {
        $scope.selected_section = angular.isNumber(section) ? $scope.sections[section] : section;
        baseService.loadTabs(section).then(function (tabs) {
            $scope.selected_tabs = tabs;
            $scope.selectTab(0);
        });
    };

    $scope.selectTab = function(tab) {
        console.log('Tab selected', tab);
        $scope.selected_tab = angular.isNumber(tab) ? $scope.selected_tabs[tab] : tab;
        $scope.showSelectedDateEnd = $scope.selected_tab.showEndDate;
        updateData([$scope.selectedDateStart, $scope.selectedDateEnd]);
    };
        
}]);