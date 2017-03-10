app.config(["$routeProvider", function($routeProvider) {
	$routeProvider
		.when("/", {
			controller: "HomeController",
			templateUrl: "/views/home",
		})
		.otherwise({
			redirectTo: "/"
		});
}]);
