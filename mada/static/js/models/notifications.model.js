angular.module('models.module')
.service('notificationModel', ['$http', '$q', function ($http, $q) {
	var service = {};

	service.getAll = function(date) {
		date = date.toISOString().substring(0, 10);
		return $http.get('notifications/'+ date +'/all').then(function (response) {
			return response.data;
		}, function (response) {
			return $q.reject(response);
		});
	};

	return service;
}])