angular.module('directives.module')
.directive('trendscard', function () {
	return {
		replace: true,
		scope: {
			item: '='
		},
		templateUrl: '/static/js/views/trends.card.html',
		link: function(scope, element, attrs) {
			var dataHolder = element[0].getElementsByClassName("cd-data-holder")[0];
			dataHolder.onclick = function () {

				if (!scope.item.percent) {
					angular.forEach(scope.item.data, function(value, index) {
						scope.item.data[index].value = Math.round((value.value*100)/value.total);
						scope.item.data[index].compare = Math.round((value.compare*100)/value.total);
						scope.item.percent = true;
					});
				} else {
					angular.forEach(scope.item.data, function(value, index) {
						scope.item.data[index].value = Math.round((value.total*value.value)/100);
						scope.item.data[index].compare = Math.round((value.total*value.compare)/100);
						scope.item.percent = false;
					});
				}

				scope.$apply();
			};
		}
	};
});