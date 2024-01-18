const changeUrl = document.getElementById('clearGalURL').value;
const clearBtn = document.getElementById('clearBtn');
const imageListSet = []


clearBtn.addEventListener('click', (event) => {
	event.preventDefault();
	clear();
});

async function clear() {
	const csrftoken = getCookie('csrftoken');
	const response = await fetch(changeUrl, {
		
		method: "GET",
		credentials: "same-origin", 
		headers: {
			'Content-Type': 'application/json',
			'X-CSRFToken': csrftoken
		}
		
	});
	
	if (!response.ok) {
		alert('refesh and retry, if the issue persist pelase contact the admin');
	} else {
		const imageList = await response.json();
		imageClear(imageList.imgList, csrftoken);
	};

};

async function imageClear(imageListSet, csrftoken){
	for (i = 0; i < imageListSet.length; ++i) {
		var checkedImg = document.getElementById('id_check'+imageListSet[i]);
		if (checkedImg) {
			let imgDiv = checkedImg.parentNode;
			imgDiv.checked = false;
			imgDiv.classList.remove("image-card-a");
			imgDiv.classList.add("image-card");
		}

		const response = await fetch(changeUrl, {
			
			method: "POST",
			credentials: "same-origin", 
			body: JSON.stringify({ 'id': imageListSet[i] }),
			headers: {
				'Content-Type': 'application/json',
				'X-CSRFToken': csrftoken
			}
			
		});

		if (!response.ok) {
			alert('refesh and retry, if the issue persist pelase contact the admin');
		} 

	};
}