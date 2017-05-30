'use strict';

var myapp = angular.module('myapp', []);

myapp.factory('User', ["$http", function($http){
	var obj = {};
	obj.authenticate = function(userData){
		console.log(userData);
		return $http.get("http://localhost:8000/accounts/logging/?email="+userData.email+"&password="+userData.password);
	};

	return obj;
}]);

myapp.controller('LoginCtrl', ["$scope", "User",
	function($scope, User){
		$scope.user = {};
		$scope.loginMsg = "";
		$scope.loginStatus = false;

		$scope.authenticate = function(){
			var result = User.authenticate($scope.user);
			result.then(function(response){
				var d = response.data;
				if(d.status === 'SUCCESS')
				{
					$scope.loginStatus = true;
					$scope.loginMsg = d.message;
				}
				else
				{
					$scope.loginStatus = false;
					$scope.loginMsg = d.message;
				}
			}, 
				function(error){
					console.error("There is an error: ", error);
				});
		};
	}]);