(function(){
  'use strict';

  angular.module('users.module')
         .service('userService', ['$q', UserService]);

  /**
   * Users DataService
   * Uses embedded, hard-coded data model; acts asynchronously to simulate
   * remote data service call(s).
   *
   * @returns {{loadAll: Function}}
   * @constructor
   */
  function UserService($q){
    var service = {};

    var sections = [
      {
        name: 'Social',
        avatar: 'svg-1',
        content: 'Understand social behavior of user on MagicPin. Currently concentrates on Profile Views'
      },
      {
        name: 'Transactions',
        avatar: 'svg-2',
        content: 'Understand when user transacts on MagicPin'
      },
      {
        name: 'Notifications',
        avatar: 'svg-3',
        content: "What are the returns of those notifications that you configured"
      },
      // {
      //   name: 'Lawrence Ray',
      //   avatar: 'svg-4',
      //   content: 'Scratch the furniture spit up on light gray carpet instead of adjacent linoleum so eat a plant, kill a hand pelt around the house and up and down stairs chasing phantoms run in circles, or claw drapes. Always hungry pelt around the house and up and down stairs chasing phantoms.'
      // },
      // {
      //   name: 'Ernesto Urbina',
      //   avatar: 'svg-5',
      //   content: 'Webtwo ipsum dolor sit amet, eskobo chumby doostang bebo. Bubbli greplin stypi prezi mzinga heroku wakoopa, shopify airbnb dogster dopplr gooru jumo, reddit plickers edmodo stypi zillow etsy.'
      // },
      // {
      //   name: 'Gani Ferrer',
      //   avatar: 'svg-6',
      //   content: "Lebowski ipsum yeah? What do you think happens when you get rad? You turn in your library card? Get a new driver's license? Stop being awesome? Dolor sit amet, consectetur adipiscing elit praesent ac magna justo pellentesque ac lectus. You don't go out and make a living dressed like that in the middle of a weekday. Quis elit blandit fringilla a ut turpis praesent felis ligula, malesuada suscipit malesuada."
      // }
    ];

    var tabs = [
      [{'title': 'All'}, {'title': 'Users'}, {'title': 'Merchants'}],
      [{'title': 'All'}, {'title': 'Started'}, {'title': 'Completed'}],
      [{'title': 'All'}, {'title': 'Social'}, {'title': 'Transactional'}]
    ]

    service.loadAllSections = function() {
      return $q.when(sections);
    }

    service.loadTabs = function (index) {
      return $q.when(tabs[index]);
    }

    return service;
  }

})();
