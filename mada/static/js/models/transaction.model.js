angular.module('models.module')
.service('txnModel', ['$http', '$q', function ($http, $q) {
	var service = {};

	service.getAll = function(date) {
		date = date.toISOString().substring(0, 10);
		return $http.get('transactions/'+ date +'/all').then(function (response) {
			return response.data;
		}, function (response) {
			console.log("Model: Failed", response);
			return $q.reject(response);
		});
	};

	service.getStarted = function(date) {
		date = date.toISOString().substring(0, 10);
		return $http.get('transactions/'+ date +'/started').then(function (response) {
			return response.data;
		}, function (response) {
			console.log("Model: Failed", response);
			return $q.reject(response);
		});
	};

	service.getCompleted = function(date) {
		date = date.toISOString().substring(0, 10);
		return $http.get('transactions/'+ date +'/completed').then(function (response) {
			return response.data;
		}, function (response) {
			return $q.reject(response);
		});
	};

	service.getCompletedDrop = function(date) {
		date = date.toISOString().substring(0, 10);
		return $http.get('transactions/'+ date +'/completed-drop').then(function (response) {
			return response.data;
		}, function (response) {
			return $q.reject(response);
		});
	};

	return service;
}])