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
	    dataSource: socialService.getAll
	  },
	  {
	    name: 'Transactions',
	    avatar: 'svg-2',
	    content: 'Understand when user transacts on MagicPin',
	    dataSource: txnService.getAll
	  },
	  {
	    name: 'Notifications',
	    avatar: 'svg-3',
	    content: "What are the returns of those notifications that you configured",
	    dataSource: notificationService.getAll
	  }
	];

	var tabs = [
	  [{'title': 'All'},],
	  [{'title': 'All'}, {'title': 'Funnel'}],
	  [{'title': 'All'}]
	]

	service.loadAllSections = function() {
	  return $q.when(sections);
	}

	service.loadTabs = function (index) {
	  return $q.when(tabs[index]);
	}

	return service;
}])