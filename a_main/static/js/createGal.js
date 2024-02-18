const displayForm = document.getElementById('CreateGalForm');
const newDisplayUrl = document.getElementById('createDisplayURL').value;

displayForm.addEventListener('submit', (submited) => {
	submited.preventDefault();

	const namedDisplay = document.getElementById('id_create_gallery').value;
	let formData = {'name' : namedDisplay}
	const csrfGet = getCookie('csrftoken');
	fetch(newDisplayUrl, {
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
		document.location.reload();
	  })

    .catch(error => {
        // Handle errors
        console.error('Error:', error);
    });
})
