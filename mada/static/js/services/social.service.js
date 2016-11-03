angular.module('services.module')
.service('socialService', [
	'$q',
	'socialModel',
	function ($q, socialModel) {

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
		return socialModel.getAll(date).then(function (data) {
			var dau_likes = {'title': "Likes: All Users"};
			var nu_likes = {'title': "Likes: New Users"};
			var dau_comments = {'title': "Comments: All Users"};
			var nu_comments = {'title': "Comments: New Users"};
			var dau_shares = {'title': "Shares: All Users"};
			var nu_shares = {'title': "Shares: New Users"};
			var dau_profile_views = {'title': "Profile Views: All Users"};
			var nu_profile_views = {'title': "Profile Views: New Users"};
			console.log("Got data: ", data);
			var result = bindData(dau_likes, nu_likes, data.likes);
			result = result.concat(bindData(dau_comments, nu_comments, data.comments));
			result = result.concat(bindData(dau_shares, nu_shares, data.shares));
			result = result.concat(bindData(dau_profile_views, nu_profile_views, data.profile_views));
			console.log("result: ", result);
			return result;
		}, function (response) {
			return $q.reject(response);
		});
	}

	return service;
}])