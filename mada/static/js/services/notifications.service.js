angular.module('services.module')
.service('notificationService', [
	'$q',
	'notificationModel',
	function ($q, notificationModel) {

	function bindData (dau, nu, data) {
		dau.dau = data.dau_total;
		dau.nu = data.nu_total;
		dau.total = data.dau_total;

		nu.dau = data.dau_total;
		nu.nu = data.nu_total;
		nu.total = data.nu_total;

		var dau_data = [];
		var nu_data = [];

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
		return notificationModel.getAll(date).then(function (data) {
			if (!data || data.length == 0) {
				return $q.reject();
			}

			var dau_opens = {'title': "Opened: All Users"};
			var nu_opens = {'title': "Opened: New Users"};
			var dau_rejects = {'title': "Rejected: All Users"};
			var nu_rejects = {'title': "Rejected: New Users"};
			var dau_opens_social = {'title': "Opened Social: All Users"};
			var nu_opens_social = {'title': "Opened Social: New Users"};
			var dau_rejects_social = {'title': "Rejected Social: All Users"};
			var nu_rejects_social = {'title': "Rejected Social: New Users"};
			var dau_opens_commerce = {'title': "Opened Commerce: All Users"};
			var nu_opens_commerce = {'title': "Opened Commerce: New Users"};
			var dau_rejects_commerce = {'title': "Rejected Commerce: All Users"};
			var nu_rejects_commerce = {'title': "Rejected Commerce: New Users"};
			
			var result = bindData(dau_opens, nu_opens, data.opens);
			result = result.concat(bindData(dau_rejects, nu_rejects, data.rejects));
			result = result.concat(bindData(dau_opens_social, nu_opens_social, data.opens_social));
			result = result.concat(bindData(dau_opens_commerce, nu_opens_commerce, data.opens_commerce));
			result = result.concat(bindData(dau_rejects_social, nu_rejects_social, data.rejects_social));
			result = result.concat(bindData(dau_rejects_commerce, nu_rejects_commerce, data.rejects_commerce));
			console.log("result: ", result);
			return result;
		}, function (response) {
			return $q.reject(response);
		});
	}

	return service;
}])