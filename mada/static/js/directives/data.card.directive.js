angular.module('directives.module')
.directive('datacard', function () {
	return {
		replace: true,
		scope: {
			item: '='
		},
		templateUrl: '/static/js/views/data.card.html',
		link: function(scope, element, attrs) {
			var dataHolder = element[0].getElementsByClassName("cd-data-holder")[0];
			dataHolder.onclick = function () {

				if (!scope.item.percent) {
					angular.forEach(scope.item.data, function(value, index) {
						scope.item.data[index].value = Math.round((value.value*100)/scope.item.total);
						scope.item.data[index].compare = Math.round((value.compare*100)/scope.item.total);
						scope.item.percent = true;
					});
				} else {
					angular.forEach(scope.item.data, function(value, index) {
						scope.item.data[index].value = Math.round((scope.item.total*value.value)/100);
						scope.item.data[index].compare = Math.round((scope.item.total*value.compare)/100);
						scope.item.percent = false;
					});
				}

				scope.$apply();
			};
		}
	};
});