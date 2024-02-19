//-------------------------------//-------------------------------//-------------------------------//
// Group DOM element selections
//-------------------------------//-------------------------------//-------------------------------//
const submitButton = document.getElementById('submit');
const formBox = document.getElementById('formBox');
const imageForm = document.getElementById('imageForm');
const uploadAnimationDiv1 = document.getElementById('uploadAnimation1');
const uploadAnimationDiv2 = document.getElementById('uploadAnimation2');
const uploadAnimationDiv3 = document.getElementById('uploadAnimation3');
const cf_id = document.getElementsByClassName('hiddenImage');
// urls
const api_url = document.getElementById('apiUrl').value
const tagAPIURL = document.getElementById('apiTagUrl').value
const displayAPIURL = document.getElementById('apiGalleryUrl').value
const redirect_url = document.getElementById('redirect').value
const error_url = document.getElementById('errorUrl').value
// loaders 
const loadValid = document.getElementById('validateImage');
const tagValid = document.getElementById('validateTags');
const displayValid = document.getElementById('validateGallery');

const id_list = []

for (i = 0; i < cf_id.length; ++i){
	id_list.push(cf_id[i].value);
}
//console.log(id_list)

//-------------------------------//-------------------------------//-------------------------------//
// backend Post request, sending the form data, and reutnring a set of cf ids and a batch token
//-------------------------------//-------------------------------//-------------------------------//

submitButton.addEventListener( 'click', async (event) => {
	
	event.preventDefault();
	formBox.classList.add('display-off');
	uploadAnimationDiv1.classList.remove('noshow');
	loadValid.style.display = 'flex';
	const data = []
	if (titleValue === '') {

        alert('Please enter a title.');
        return;
    }
	
	const titleElement = document.getElementById('id_title');
	const tagElement = document.getElementById('id_tag');
	const displayElement = document.getElementById('id_display');
	const projectElement = document.getElementById('id_project_id');
	const selectedTags = Array.from(tagElement.selectedOptions).map(option => option.value);
	const selectedDisplay = Array.from(displayElement.selectedOptions).map(option => option.value);

	data.push({'title' : titleElement.value});
	data.push({'project': projectElement.value});
	data.push({'cf_id': id_list});

    const imageData = await updateImageMeta(data);

    // Check if selectedTags exist
    if (selectedTags.length > 0) {
		tagValid.style.display = 'flex';
		uploadAnimationDiv2.classList.remove('noshow');
        await updateTagMeta({ 'imageList': imageData, 'tags': selectedTags });
    }

    // Check if selectedDisplay exist
    if (selectedDisplay.length > 0) {
		displayValid.style.display = 'flex';
		uploadAnimationDiv3.classList.remove('noshow');
        await updateDisplayMeta({ 'imageList': imageData, 'displays': selectedDisplay });
    }

    // Redirect after all async functions are completed
    window.location.href = redirect_url;
});

//-------------------------------//-------------------------------//-------------------------------//
// Handling file upload button click
//-------------------------------//-------------------------------//-------------------------------//
async function updateImageMeta(formData) {
	const listdata = { 'data': formData }
	const csrfGet = getCookie('csrftoken');
	const response = (await fetch(api_url, {
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
		return response.json();
	} else {
		alert("Issue with adding images, refresh and retry")
		return false;
		
	}

};

//-------------------------------//-------------------------------//-------------------------------//
// if tags exist, this will send a request to update the tags for the images 
//-------------------------------//-------------------------------//-------------------------------//
async function updateTagMeta(formData) {

	const csrfGet = getCookie('csrftoken');
	const response = (await fetch(tagAPIURL, {
            method: 'POST',
			body: JSON.stringify(formData),
            credentials: 'same-origin',
            headers: {
                'token_request': 'token_request',
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfGet
            },
	}));
	
	if (response.ok){
		return;
	} else {
		alert("Issue with adding tags, refresh and retry")
		return false;
		
	}
};
//-------------------------------//-------------------------------//-------------------------------//
// if gallery/galleries are selected, this will send a request to update the display images 
//-------------------------------//-------------------------------//-------------------------------//
async function updateDisplayMeta(formData) {

	const csrfGet = getCookie('csrftoken');
	const response = (await fetch(displayAPIURL, {
            method: 'POST',
			body: JSON.stringify(formData),
            credentials: 'same-origin',
            headers: {
                'token_request': 'token_request',
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfGet
            },
	}));
	
	if (response.ok){
		return;

	} else {
		alert("Issue with adding gallery, refresh and retry")
		return false;
		
	}
};