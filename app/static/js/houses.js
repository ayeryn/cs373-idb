// app.js
angular.module('sortApp', [])

.controller('mainController', function($scope) {
  $scope.sortType     = 'name'; // set the default sort type
  $scope.sortReverse  = false;  // set the default sort order
  $scope.searchNames   = '';     // set the default search/filter term
  
  // create the list of sushi rolls 
  $scope.sushi = [
    { name: 'House Stark of Winterfell', region: 'The North', words: 'Winter is Coming', lord: 'N/A', heir: 'N/A', overlord: 'House Baratheon of Kings Landing' },
    { name: 'House Baratheon of Kings Landing', region: 'The Crownlands', words: 'Ours is the Fury', lord: 'Tommen Baratheon', heir: 'Myrcella Baratheon', overlord: 'House Baratheon of Dragonstone' },
    { name: 'House Lannister of Casterly Rock', region: 'The Westerlands', words: 'Hear Me Roar!', lord: 'Cersei Lannister', heir: 'N/A', overlord: 'House Baratheon of Kings Landing' }
  ];
  
});
