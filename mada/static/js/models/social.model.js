angular.module('models.module')
.service('socialModel', ['$http', '$q', function ($http, $q) {
	var service = {};

	service.getAll = function(date) {
		date = date.toISOString().substring(0, 10);
		return $http.get('social/'+ date +'/all').then(function (response) {
			return response.data;
		}, function (response) {
			return $q.reject(response);
		});
	};

	service.getLikes = function(date) {
		date = date.toISOString().substring(0, 10);
		return $http.get('social/'+ date +'/likes').then(function (response) {
			return response.data;
		}, function (response) {
			return $q.reject(response);
		});
	};

	service.getComments = function(date) {
		date = date.toISOString().substring(0, 10);
		return $http.get('social/'+ date +'/comments').then(function (response) {
			return response.data;
		}, function (response) {
			return $q.reject(response);
		});
	};

	service.getShares = function(date) {
		date = date.toISOString().substring(0, 10);
		return $http.get('social/'+ date +'/shares').then(function (response) {
			return response.data;
		}, function (response) {
			return $q.reject(response);
		});
	};

	service.getProfileViews = function(date) {
		date = date.toISOString().substring(0, 10);
		return $http.get('social/'+ date +'/profile-views').then(function (response) {
			return response.data;
		}, function (response) {
			return $q.reject(response);
		});
	};

	return service;
}])