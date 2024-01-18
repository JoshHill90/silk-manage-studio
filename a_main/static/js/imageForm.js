//-------------------------------//-------------------------------//-------------------------------//
// Group DOM element selections
//-------------------------------//-------------------------------//-------------------------------//
const submitButton = document.getElementById('submit');
const formBox = document.getElementById('formBox');
const imageForm = document.getElementById('imageForm');
const uploadAnimationDiv = document.getElementById('uploadAnimation');
const cf_id = document.getElementsByClassName('hiddenImage');
const api_url = document.getElementById('apiUrl')
const redirect_url = document.getElementById('redirect').value
const error_url = document.getElementById('errorUrl').value
const loadValid = document.getElementById('validate');
const id_list = []

for (i = 0; i < cf_id.length; ++i){
	id_list.push(cf_id[i].value);
}
//console.log(id_list)

//-------------------------------//-------------------------------//-------------------------------//
// backend Post request, sending the form data, and reutnring a set of cf ids and a batch token
//-------------------------------//-------------------------------//-------------------------------//

submitButton.addEventListener( 'click', (event) => {
	
	event.preventDefault();
	formBox.classList.add('display-off');
	uploadAnimationDiv.classList.remove('noshow');
	loadValid.style.display = 'flex';
	const data = []
	
	
	const titleElement = document.getElementById('id_title');
	const tagElement = document.getElementById('id_tag');
	const displayElement = document.getElementById('id_display');
	const projectElement = document.getElementById('id_project_id');
	const selectedTags = Array.from(tagElement.selectedOptions).map(option => option.value);
	const selectedDisplay = Array.from(displayElement.selectedOptions).map(option => option.value);

	data.push({'title' : titleElement.value});
	data.push({'tag': selectedTags});
	data.push({'project': projectElement.value});
	data.push({'display': selectedDisplay});
	data.push({'cf_id': id_list});
	updateImageMeta(data);
});

//-------------------------------//-------------------------------//-------------------------------//
// Handling file upload button click
//-------------------------------//-------------------------------//-------------------------------//
async function updateImageMeta(formData) {
	const listdata = { 'data': formData }
	const csrfGet = getCookie('csrftoken');
	const url = api_url['value']
	const response = (await fetch(url, {
            method: 'POST',
			body: JSON.stringify(listdata),
            credentials: 'same-origin',
            headers: {
                'token_request': 'token_request',
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfGet
            },
	}));
	
	if (response.ok){
		window.location.href = redirect_url
	} else {
		alert("refresh and retry")
		return false;
		
	}


	
};



