function charSwitch(x) {
	switch (x) {
		case 1:
			document.getElementById("selected-character-id").src="https://www.3dtotal.com/admin/new_cropper/gallery_736/drogo_f05.jpg";
			document.getElementById("drink-button").innerHTML="Khal Drogo wants Whiskey!";
			break;
		case 2:
			document.getElementById("selected-character-id").src="http://vignette4.wikia.nocookie.net/gameofthrones/images/c/c0/Arya_Stark_profile_Season4.jpg/revision/latest?cb=20140626201536";
			document.getElementById("drink-button").innerHTML="Something with Vodka please!";
			break;
		case 3:
			document.getElementById("selected-character-id").src="http://cdn-img.instyle.com/sites/default/files/styles/684xflex/public/images/2016/04/042216-cersei-lannister-lead-new.jpg?itok=8TPG8WNQ";
			document.getElementById("drink-button").innerHTML="Only the best (Gin) for the Queen";
			break;
		case 4:
			document.getElementById("selected-character-id").src="https://vignette4.wikia.nocookie.net/gameofthrones/images/8/88/Daenerys-0.jpg/revision/latest/scale-to-width-down/350?cb=20170106122450";
			document.getElementById("drink-button").innerHTML="My dragons require Rum!";
			break;
		case 5:
			document.getElementById("selected-character-id").src="https://qph.ec.quoracdn.net/main-qimg-0c8c7540509baf623b5397b8a564f36c";
			document.getElementById("drink-button").innerHTML="You know how Little Finger does Tequilla...";
			break;
	}
}
