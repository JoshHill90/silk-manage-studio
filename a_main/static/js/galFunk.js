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
		
		imageClear();
	};

};

async function imageClear(){
	var checkedImg = document.querySelectorAll('.checkImage');;
	for (i = 0; i < checkedImg.length; ++i) {
		
		if (checkedImg[i].checked == true) {
			let imgDiv = checkedImg[i].parentNode;
			imgDiv.checked = false;
			imgDiv.classList.remove("image-card-a");
			imgDiv.classList.add("image-card");
		}

	};
}