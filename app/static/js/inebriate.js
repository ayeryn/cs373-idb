function charSwitch(x) {
	switch (x) {
		case 1:
			document.getElementById("selected-character-id").src="static/images/khal.jpg";
			document.getElementById("drink-button").innerHTML="Khal Drogo wants Whiskey!";
			document.getElementById("drink-button").disabled = false;
			break;
		case 2:
			document.getElementById("selected-character-id").src="static/images/arya.jpg";
			document.getElementById("drink-button").innerHTML="Something with Vodka please!";
			document.getElementById("drink-button").disabled = false;
			break;
		case 3:
			document.getElementById("selected-character-id").src="static/images/cersei.jpg";
			document.getElementById("drink-button").innerHTML="Only the best Red Wine for the Queen";
			document.getElementById("drink-button").disabled = false;
			break;
		case 4:
			document.getElementById("selected-character-id").src="static/images/dany.jpg";
			document.getElementById("drink-button").innerHTML="My dragons require Rum!";
			document.getElementById("drink-button").disabled = false;
			break;
		case 5:
			document.getElementById("selected-character-id").src="static/images/littlefinger.jpg";
			document.getElementById("drink-button").innerHTML="You know how Little Finger does Tequilla...";
			document.getElementById("drink-button").disabled = false;
			break;
		case 6:
			document.getElementById("selected-character-id").src="static/images/varys.jpg";
			document.getElementById("drink-button").innerHTML="I hear birds whispering something about gin...";
			document.getElementById("drink-button").disabled = false;
			break;
		case 7:
			document.getElementById("selected-character-id").src="static/images/sansa.jpg";
			document.getElementById("drink-button").innerHTML="I guess I'll try some White Wine then";
			document.getElementById("drink-button").disabled = false;
			break;
		case 8:
			document.getElementById("selected-character-id").src="static/images/tyrion.jpg";
			document.getElementById("drink-button").innerHTML="What's the strongest thing you have?";
			document.getElementById("drink-button").disabled = false;
			break;
		case 9:
			document.getElementById("selected-character-id").src="static/images/robert.jpg";
			document.getElementById("drink-button").innerHTML="I'll take that port and pretty girl HAHA";
			document.getElementById("drink-button").disabled = false;
			break;
		case 10:
			document.getElementById("selected-character-id").src="static/images/jon.jpg";
			document.getElementById("drink-button").innerHTML="Beer to cheers the King in the North! ";
			document.getElementById("drink-button").disabled = false;
			break;
	}
}
