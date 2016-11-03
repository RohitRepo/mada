angular.module('services.module')
.service('socialService', [
	'$q',
	'socialModel',
	function ($q, socialModel) {

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
			var result = bindAllData(dau_likes, nu_likes, data.likes);
			result = result.concat(bindAllData(dau_comments, nu_comments, data.comments));
			result = result.concat(bindAllData(dau_shares, nu_shares, data.shares));
			result = result.concat(bindAllData(dau_profile_views, nu_profile_views, data.profile_views));
			console.log("result: ", result);
			return result;
		}, function (response) {
			return $q.reject(response);
		});
	}

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
		return socialModel.getTrends(date_start, date_end).then(function (data) {
			var dau_likes = {'title': "Likes: All Users"};
			var nu_likes = {'title': "Likes: New Users"};
			var dau_comments = {'title': "Comments: All Users"};
			var nu_comments = {'title': "Comments: New Users"};
			var dau_shares = {'title': "Shares: All Users"};
			var nu_shares = {'title': "Shares: New Users"};
			var dau_profile_views = {'title': "Profile Views: All Users"};
			var nu_profile_views = {'title': "Profile Views: New Users"};
			console.log("Got data: ", data);
			var result = bindTrendsData(dau_likes, nu_likes, data.likes);
			result = result.concat(bindTrendsData(dau_comments, nu_comments, data.comments));
			result = result.concat(bindTrendsData(dau_shares, nu_shares, data.shares));
			result = result.concat(bindTrendsData(dau_profile_views, nu_profile_views, data.profile_views));
			console.log("result: ", result);
			return result;
		}, function (response) {
			return $q.reject(response);
		});
	}

	return service;
}])