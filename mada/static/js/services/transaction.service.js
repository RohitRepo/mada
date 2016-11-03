angular.module('services.module')
.service('txnService', [
	'$q',
	'txnModel',
	function ($q, txnModel) {

	function bindAllData (dau, nu, data) {
		var dau_data = [];
		var nu_data = [];

		if (data == undefined) {
			return [dau, nu];
		}

		dau.dau = data.dau_total;
		dau.nu = data.nu_total;
		dau.total = data.dau_total;
		dau.type = 'ALL';

		nu.dau = data.dau_total;
		nu.nu = data.nu_total;
		nu.total = data.nu_total;
		nu.type = 'ALL';

		dau_data.push({"title": "MONTH", 'value': data.month_dau, 'compare': data.month_dau_compare});
		dau_data.push({"title": "WEEK", 'value': data.week_dau, 'compare': data.week_dau_compare});
		dau_data.push({"title": "BEFORE", 'value': data.before_dau, 'compare': data.before_dau_compare});
		dau_data.push({"title": "YESTERDAY", 'value': data.yesterday_dau, 'compare': data.yesterday_dau_compare});
		dau_data.push({"title": "TODAY", 'value': data.dau, 'compare': data.dau_compare});
		dau.data = dau_data;

		nu_data.push({"title": "MONTH", 'value': data.month_nu, 'compare': data.month_nu_compare});
		nu_data.push({"title": "WEEK", 'value': data.week_nu, 'compare': data.week_nu_compare});
		nu_data.push({"title": "BEFORE", 'value': data.before_nu, 'compare': data.before_nu_compare});
		nu_data.push({"title": "YESTERDAY", 'value': data.yesterday_nu, 'compare': data.yesterday_nu_compare});
		nu_data.push({"title": "TODAY", 'value': data.nu, 'compare': data.nu_compare});
		nu.data = nu_data;

		return [dau, nu];
	};

	var service = {};

	service.getAll = function (date) {
		return txnModel.getAll(date).then(function (data) {
			var dau_started = {'title': "Transaction Started: All Users"};
			var nu_started = {'title': "Transaction Started: New Users"};
			var dau_completed = {'title': "Transaction Completed: All Users"};
			var nu_completed = {'title': "Transaction Completed: New Users"};
			var dau_drop = {'title': "Transaction Drop: All Users"};
			var nu_drop = {'title': "Transaction Drop: New Users"};
			var result = bindAllData(dau_started, nu_started, data.started);
			result = result.concat(bindAllData(dau_completed, nu_completed, data.completed));
			result = result.concat(bindAllData(dau_drop, nu_drop, data.completed_drop));
			return result;
		}, function (response) {
			return $q.reject(response);
		});
	};

	function bindTrendsData (dau, nu, data) {

		if (data == undefined) {
			return [dau, nu];
		}

		dau.data = [];
		nu.data = [];

		dau.type = 'TRENDS';
		nu.type = 'TRENDS';


		angular.forEach(data, function (item, key) {
			dau.data.push({
				'value' : item.dau,
				'compare' : item.dau_compare,
				'total': item.dau_total,
				'dated': item.dated,
			});

			nu.data.push({
				'value' : item.nu,
				'compare' : item.nu_compare,
				'total': item.nu_total,
				'dated': item.dated,
			});

		});

		return [dau, nu];
	};

	service.getTrends = function (date_start, date_end) {
		return txnModel.getTrends(date_start, date_end).then(function (data) {
			var dau_started = {'title': "Transaction Started: All Users"};
			var nu_started = {'title': "Transaction Started: New Users"};
			var dau_completed = {'title': "Transaction Completed: All Users"};
			var nu_completed = {'title': "Transaction Completed: New Users"};
			var dau_drop = {'title': "Transaction Drop: All Users"};
			var nu_drop = {'title': "Transaction Drop: New Users"};
			console.log("Transactions ", data);
			var result = bindTrendsData(dau_started, nu_started, data.started);
			result = result.concat(bindTrendsData(dau_completed, nu_completed, data.completed));
			result = result.concat(bindTrendsData(dau_drop, nu_drop, data.completed_drop));
			return result;
		}, function (response) {
			return $q.reject(response);
		});
	}

	// service.getStarted = function (date) {
	// 	return txnModel.getStarted(date).then(function (data) {
	// 		var dau = {'title': "Transaction Started: All Users"};
	// 		var nu = {'title': "Transaction Started: New Users"};
	// 		return bindData(dau, nu, data);
	// 	}, function (response) {
	// 		return $q.reject(response);
	// 	});
	// }

	// service.getCompleted = function (date) {
	// 	return txnModel.getCompleted(date).then(function (data) {
	// 		var dau = {'title': "Transaction Completed: All Users"};
	// 		var nu = {'title': "Transaction Completed: New Users"};
	// 		return bindData(dau, nu, data);
	// 	}, function (response) {
	// 		return $q.reject(response);
	// 	});
	// }

	// service.getCompletedDrop = function (date) {
	// 	return txnModel.getCompletedDrop(date).then(function (data) {
	// 		var dau = {'title': "Transaction Drop: All Users"};
	// 		var nu = {'title': "Transaction Drop: New Users"};
	// 		return bindData(dau, nu, data);
	// 	}, function (response) {
	// 		return $q.reject(response);
	// 	});
	// }

	return service;
}])