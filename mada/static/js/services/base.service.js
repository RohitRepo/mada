angular.module('services.module')
.service('baseService', [
	'$q',
	'txnService',
	'socialService',
	'notificationService',
	function ($q, txnService, socialService, notificationService) {
	var service = {};

	var sections = [
	  {
	    name: 'Social',
	    avatar: 'svg-1',
	    content: 'Understand social behavior of user on MagicPin.',
	    
	  },
	  {
	    name: 'Transactions',
	    avatar: 'svg-2',
	    content: 'Understand when user transacts on MagicPin',
	    
	  },
	  {
	    name: 'Notifications',
	    avatar: 'svg-3',
	    content: "What are the returns of those notifications that you configured",
	    
	  }
	];

	var tabs = [
	[{
	  	'title': 'All',
		'dataSource': function (dates) {
			return socialService.getAll(dates[0]);
		},
	},{
	  	'title': 'Trends',
	  	'showEndDate': true,
		'dataSource': function (dates) {
			return socialService.getTrends(dates[0], dates[1]);
		},
	},],
	[{
	  	'title': 'All',
		'dataSource': function (dates) {
			return txnService.getAll(dates[0]);
		}
	},{
	  	'title': 'Trends',
	  	'showEndDate': true,
		'dataSource': function (dates) {
			return txnService.getTrends(dates[0], dates[1]);
		}
	},],
	[{
	  	'title': 'All',
		'dataSource': function (dates) {
			return notificationService.getAll(dates[0]);
		}
	},]
	]

	service.loadAllSections = function() {
	  return $q.when(sections);
	}

	service.loadTabs = function (index) {
	  return $q.when(tabs[index]);
	}

	return service;
}])