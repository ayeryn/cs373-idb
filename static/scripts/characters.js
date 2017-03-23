// characters.js
angular.module('sortApp', [])

.controller('mainController', function($scope) {
  $scope.sortType     = 'name'; // set the default sort type
  $scope.sortReverse  = false;  // set the default sort order
  $scope.searchNames   = '';     // set the default search/filter term
  
  // create the list of sushi rolls 
  $scope.chars = [
    { name: 'Arya Stark', titles: 'Princess', aliases: '-', father: '-', mother: '-', spouse: '-', allegiances: 'House Stark of Winterfell', actor: 'Maise Williams'},
    { name: 'Cersei Lannister', titles: 'Light of the West, Queen Dowager, Protector of the Realm, Lady of Casterly Rock, Queen Regent', aliases: '-', father: '-', mother: '-', spouse: 'Robert I Baratheon', allegiances: 'House Lannister of Casterly Rock', actor: 'Lena Headey'},
    { name: 'Daenerys Targaryen', titles: 'Princess', aliases: '-', father: '-', mother: '-', spouse: 'Maron Nymeros Martell', allegiances: 'House Nymeros Martell of Sunspear, House Targaryen of Kings Landing', actor: 'Emilia Clark'},
  ];
});