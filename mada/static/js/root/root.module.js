angular.module("numadaApp", ['ngMaterial', 'services.module', 'directives.module'])
.config(['$mdThemingProvider',
	'$mdIconProvider',
	'$interpolateProvider',
	'$httpProvider',
	function($mdThemingProvider, $mdIconProvider, $interpolateProvider, $httpProvider){

    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]')

	// csrf for django
	$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
	$httpProvider.defaults.xsrfCookieName = 'csrftoken';

    $mdIconProvider
        .defaultIconSet("/static/assets/svg/avatars.svg", 128)
        .icon("menu"       , "/static/assets/svg/menu.svg"        , 24)
        .icon("share"      , "/static/assets/svg/share.svg"       , 24)
        .icon("google_plus", "/static/assets/svg/google_plus.svg" , 512)
        .icon("hangouts"   , "/static/assets/svg/hangouts.svg"    , 512)
        .icon("twitter"    , "/static/assets/svg/twitter.svg"     , 512)
        .icon("phone"      , "/static/assets/svg/phone.svg"       , 512);

        $mdThemingProvider.theme('default')
            .primaryPalette('brown')
            .accentPalette('red');

}]);