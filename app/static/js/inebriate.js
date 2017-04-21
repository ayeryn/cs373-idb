var divs = ["modal0","modal1","modal2","modal3","modal4","modal5","modal6","modal7","modal8","modal9"];
var visibleDivId = null;
function toggleVisibility(divId) {
  if(visibleDivId === divId) {
    //visibleDivId = null;
  } else {
    visibleDivId = divId;
  }
  hideNonVisibleDivs();
}
function hideNonVisibleDivs() {
  var i, divId, div;
  for(i = 0; i < divs.length; i++) {
    divId = divs[i];
    div = document.getElementById(divId);
    if(visibleDivId === divId) {
      div.style.display = 'block';
    } else {
      div.style.display = 'none';
    }
  }
}

function charSwitch(x) {
	switch (x) {
		case 1:
			document.getElementById("selected-character-id").src="static/images/khal.jpg";
			document.getElementById("drink-button").innerHTML="Khal Drogo wants Whiskey!";
			document.getElementById("drink-button").disabled = false;
			document.getElementById("modal-title").innerHTML="Whiskey Drinks for the Khal";
			break;
		case 2:
			document.getElementById("selected-character-id").src="static/images/arya.jpg";
			document.getElementById("drink-button").innerHTML="Something with Vodka please!";
			document.getElementById("drink-button").disabled = false;
			document.getElementById("modal-title").innerHTML="Voda Drinks that Arya is definitely too young for";
			break;
		case 3:
			document.getElementById("selected-character-id").src="static/images/cersei.jpg";
			document.getElementById("drink-button").innerHTML="Only the best Red Wine for the Queen";
			document.getElementById("drink-button").disabled = false;
			document.getElementById("modal-title").innerHTML="Red Wine Drinks for the Iron Throne incumbent";
			break;
		case 4:
			document.getElementById("selected-character-id").src="static/images/dany.jpg";
			document.getElementById("drink-button").innerHTML="My dragons require Rum!";
			document.getElementById("drink-button").disabled = false;
			document.getElementById("modal-title").innerHTML="Rum Drinks for the Mother of Dragons";
			break;
		case 5:
			document.getElementById("selected-character-id").src="static/images/littlefinger.jpg";
			document.getElementById("drink-button").innerHTML="You know how Little Finger does Tequila...";
			document.getElementById("drink-button").disabled = false;
			document.getElementById("modal-title").innerHTML="Tequila Drinks for Baelish";
			break;
		case 6:
			document.getElementById("selected-character-id").src="static/images/varys.jpg";
			document.getElementById("drink-button").innerHTML="I hear birds whispering something about gin...";
			document.getElementById("drink-button").disabled = false;
			document.getElementById("modal-title").innerHTML="Gin Drinks for Varys and his birds";
			break;
		case 7:
			document.getElementById("selected-character-id").src="static/images/sansa.jpg";
			document.getElementById("drink-button").innerHTML="I guess I'll try some White Wine then";
			document.getElementById("drink-button").disabled = false;
			document.getElementById("modal-title").innerHTML="White Wine Drinks for Sansa";
			break;
		case 8:
			document.getElementById("selected-character-id").src="static/images/tyrion.jpg";
			document.getElementById("drink-button").innerHTML="What's the strongest thing you have?";
			document.getElementById("drink-button").disabled = false;
			document.getElementById("modal-title").innerHTML="Bourbon Drinks that still won't be strong enough for Tyrion";
			break;
		case 9:
			document.getElementById("selected-character-id").src="static/images/robert.jpg";
			document.getElementById("drink-button").innerHTML="I'll take that port and pretty girl HAHA";
			document.getElementById("drink-button").disabled = false;
			document.getElementById("modal-title").innerHTML="Port Drinks for King Robert to take to his grave";
			break;
			break;
		case 10:
			document.getElementById("selected-character-id").src="static/images/jon.jpg";
			document.getElementById("drink-button").innerHTML="Beer to cheers the King in the North! ";
			document.getElementById("drink-button").disabled = false;
			document.getElementById("modal-title").innerHTML="Beer Drinks for our favorite guy who knows nothing!";
			break;
	}
}
