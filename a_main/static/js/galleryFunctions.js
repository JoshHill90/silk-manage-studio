const displaySettingsForm = document.getElementById('galSettingsForm');
const displaySettingsUrl = document.getElementById('settingsDisplayURL').value;
const displayDeleteForm = document.getElementById('deleteDisplayForm');
const displayDeleteUrl = document.getElementById('settingsDisplayURL').value;
const displayShareForm = document.getElementById('shareDisplayForm');
const displayShareUrl = document.getElementById('shareDisplayURL').value;
const ShareUrl = document.getElementById('ShareUrl');

displaySettingsForm.addEventListener('submit', (submited) => {
	submited.preventDefault();

	const visiableDisplay = document.getElementById('id_visiable').checked;
	const siteDisplay = document.getElementById('id_site').checked;
	const randomDisplay = document.getElementById('id_random').checked;
	const lockDisplay = document.getElementById('id_lock').checked;

	let formData = {
		'visiable' : visiableDisplay,
		'site' : siteDisplay,
		'random' : randomDisplay,
		'lock' : lockDisplay
	}

	const csrfGet = getCookie('csrftoken');

	fetch(displaySettingsUrl, {
        method: 'PUT',

        body: JSON.stringify(formData),
		credentials: 'same-origin',
        headers: {
			'token_request': 'token_request',
			'Content-Type': 'application/json',
			'X-CSRFToken': csrfGet
        },
    })
	.then(response => {
		//response check
		// if it's showing with an error, the system will toss and erro, if it's 
		if (!response.ok) {
		  throw new Error(`HTTP error! Status: please refresh and try again`);
		}
		document.location.reload();
	  })

    .catch(error => {
        // Handle errors
        console.error('Error:', error);
    });
})

displayDeleteForm.addEventListener('submit', (submited) => {
	submited.preventDefault();

	const csrfGet = getCookie('csrftoken');

	fetch(displaySettingsUrl, {
        method: 'DELETE',
		credentials: 'same-origin',
        headers: {
			'token_request': 'token_request',
			'Content-Type': 'application/json',
			'X-CSRFToken': csrfGet
        },
    })
	.then(response => {
		//response check
		// if it's showing with an error, the system will toss and erro, if it's 
		if (!response.ok) {
		  throw new Error(`HTTP error! Status: please refresh and try again`);
		}
		document.location.href = '/';
	  })

    .catch(error => {
        // Handle errors
        console.error('Error:', error);
    });
})

displayShareForm.addEventListener('submit', (submited) => {
	submited.preventDefault();

	const csrfGet = getCookie('csrftoken');
	const formData = document.getElementById('id_daysExpire').value
	fetch(displayShareUrl, {
        method: 'POST',
		body: JSON.stringify(formData),
		credentials: 'same-origin',
        headers: {
			'token_request': 'token_request',
			'Content-Type': 'application/json',
			'X-CSRFToken': csrfGet
        },
    })
	.then(response => {
		//response check
		// if it's showing with an error, the system will toss and erro, if it's 
		if (!response.ok) {
		  throw new Error(`HTTP error! Status: please refresh and try again`);
		}
		return response.json()
	  })
	.then(data => {
		ShareUrl.value = data.url
	})
    .catch(error => {
        // Handle errors
        console.error('Error:', error);
    });
})

function modalImageInfo(event, id) {
    event.preventDefault();
	document.getElementById(`ImageGalBtn${id}`).click();
	const link = document.getElementById(`img-image_link${id}`).getAttribute('value')
	const title = document.getElementById(`img-title${id}`).getAttribute('value')
	const firstName = document.getElementById(`img-first_name${id}`).getAttribute('value')
	const lastName = document.getElementById(`img-last_name${id}`).getAttribute('value')
	const project = document.getElementById(`img-project_id${id}`).getAttribute('value')

	document.getElementById('img-image_link_fild').innerHTML = link
	document.getElementById('img-title_fild').innerHTML = title
	document.getElementById('img-first_name_fild').innerHTML = `${firstName} ${lastName}`

	document.getElementById('img-project_id_fild').innerHTML = project
	document.getElementById('imgPrev').src = link



}
