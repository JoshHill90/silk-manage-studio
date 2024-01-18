//-------------------------------//-------------------------------//-------------------------------//
// Group DOM element selections
//-------------------------------//-------------------------------//-------------------------------//

const tagDiv = document.getElementById('tags');
const tagInput = document.getElementById('id_tagCreate');
const tagForm = document.getElementById('id_tag');
const displayInput = document.getElementById('id_display');
const displayTags = document.getElementsByClassName('displayOptions');
//-------------------------------//-------------------------------//-------------------------------//
// tag event listener, check for the enter key to create a new tag, 
//-------------------------------//-------------------------------//-------------------------------//

tagInput.addEventListener('keydown', function(event) {
	if (event.key == 'Enter') {
		event.preventDefault();
		const tagCol = document.createElement('div');
		tagCol.className = 'col-3'
		const tag = document.createElement('p');
		tagCol.className = 'section-item'
		const tagText = tagInput.value.trim();

		if (tagText !== '') {
			tag.innerHTML = tagText;
			tag.value = tagText;
			tag.innerHTML += ' <a><i class="delete-button fa-solid fa-circle-xmark fa-2xs"></i></a>';
			tagForm.innerHTML += `<option selected value="${tagText}">${tagText}</option>`
			tagDiv.appendChild(tagCol);
			tagCol.appendChild(tag);
			tagInput.value = '';
		}
	}

});
//-------------------------------//
// remove tags from list
//-------------------------------//
tagDiv.addEventListener('click', function(event){
	if (event.target.classList.contains('delete-button')){
		const l1 = event.target.parentNode
		const l2 = l1.parentNode;
		const l3 = l2.parentNode;
		
		const tagVal = l2.value;
		getText(l2.value)
		console.log(tagVal)
		l1.remove();
		l2.remove();
		l3.remove();
	}
});

function getText(xTagval) {

	for (let i = 0; i < tagForm.length; i++) {
		let option = tagForm.options[i];
		if (option.value == xTagval) {
			option.remove();
		}
	}
}

//-------------------------------//-------------------------------//-------------------------------//
// adds display tag
//-------------------------------//-------------------------------//-------------------------------//

function displayHandler (targetObj) {
	//console.log(targetObj.target.getAttribute('value'))
	if (targetObj.target.classList.contains('selectedcolor')){
		targetObj.target.classList.add('not-selcolor')
		targetObj.target.classList.remove('selectedcolor');
		let selectDiv = document.getElementById(targetObj.target.getAttribute('value') + 'display')
		selectDiv.selected = false
		
	} else {
		targetObj.target.classList.remove('not-selcolor');
		targetObj.target.classList.add('selectedcolor');
		let selectDiv = document.getElementById(`${targetObj.target.getAttribute('value')}display`)

		selectDiv.selected = true
	}

}
for (i = 0; i < displayTags.length; i++){
	displayTags[i].addEventListener('click', function(event){
		displayHandler(event);
	});
};
