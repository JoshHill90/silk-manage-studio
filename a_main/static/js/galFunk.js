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
		
		await imageClear();
	};

};

async function imageClear(){
	var checkedImg = document.querySelectorAll('.checkImage');
	document.getElementById('currentList').hidden = true;
	document.getElementById('viewerImage').hidden = true;

	var emptyDiv = document.getElementById('emptyText');

	const coldiv = document.createElement('div');
	coldiv.classList.add('col-12');
	emptyDiv.appendChild(coldiv);
	
	const carddiv = document.createElement('div');
	carddiv.classList.add('cardSlide', 'mt-4', 'mb-4');
	coldiv.appendChild(carddiv);

	const h1div = document.createElement('h1');
	h1div.classList.add('h1-1', 'text-center');
	h1div.innerHTML = 'Please use the gallery controls to add images.';
	carddiv.appendChild(h1div);

	for (i = 0; i < checkedImg.length; ++i) {
		
		if (checkedImg[i].checked == true) {
			let imgDiv = checkedImg[i].parentNode;
			imgDiv.checked = false;
			imgDiv.classList.remove("image-card-a");
			imgDiv.classList.add("image-card");
		}

	};
}