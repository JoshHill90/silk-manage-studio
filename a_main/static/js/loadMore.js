

const loaderRow = document.getElementById('loaderRow');
let nextPage = 1;
const url = document.getElementById('loadMore').value;
//console.log(url)
const loadBtn = document.getElementById('loadMore');
const loaderBar = document.getElementById('dotsLoader');
const gallery = document.getElementById('gallery').value;
const lastPage = document.getElementById('lastPage').value;


document.getElementById("loadMore").addEventListener("click", function(event){
	event.preventDefault();
	nextPage ++;
	const data = {'next_p': nextPage, 'keyler': 'loadMore'}
	
	const csrftoken = getCookie('csrftoken');
	loadBtn.style.display = 'none'
	loaderBar.style.display = 'flex'

	fetch(url, {
		method: 'POST', 
		body: JSON.stringify(data), 
		credentials: 'same-origin',

		headers: {
			'keyler': 'loadMore',
			'Content-Type': 'application/json',
			'X-CSRFToken': csrftoken
		}

	})
	.then(res => res.json())
	.then(responseData => {
		//console.log(nextPage, lastPage)
		if (nextPage == lastPage){
			loaderBar.style.display = 'none';
		} else {
			loaderBar.style.display = 'none';
			loadBtn.style.display = 'inline-block';
		};
		
		galleryDivs(responseData);
	}).catch(error => console.error('Error:', error));
});

function galleryDivs(galleryData) {
    const currentGal = galleryData.displaySet;
    const loaderRow = document.getElementById('loaderRow');

    for (let data of galleryData.imgObj) {
        let itemId = data.id;
        let itemTitle = data.title;
        let itemImage = data.image_link;
        let itemProject = data.project;

        const parentCol = document.createElement('div');
        parentCol.className = 'col mt-4 mb-4';

        const imageCard = document.createElement('div');

        imageCard.id = itemId;

        const itemCheckDiv = document.createElement('input');
        itemCheckDiv.className = 'noshow checkImage form-check-input';
        itemCheckDiv.type = 'checkbox';
        itemCheckDiv.name = 'checkbox' + itemId;
        itemCheckDiv.value = itemId;
        itemCheckDiv.id = 'id_check' + itemId;
        imageCard.appendChild(itemCheckDiv);

        if (currentGal.includes(parseInt(itemId))) {
            imageCard.className = 'image-card-a';
            itemCheckDiv.checked = true
        } else {
            imageCard.className = 'image-card';
            itemCheckDiv.checked = false
        }

        const imageInfoDi = document.createElement('label');
        imageInfoDi.className = 'image-card-info';
        imageInfoDi.htmlFor = 'id_check' + itemId;

        const itemImageDiv = document.createElement('img');
        itemImageDiv.src = itemImage;
        itemImageDiv.className = 'image-list';
        itemImageDiv.setAttribute('load', 'lazy');
        imageInfoDi.appendChild(itemImageDiv);

        const hiddenDivs = document.createElement('div');
        hiddenDivs.style.display = 'none';
        hiddenDivs.id = 'hiddenDivs' + itemId;

        const imgTitleDiv = document.createElement('div');
        imgTitleDiv.id = 'img-title' + itemId;
        imgTitleDiv.innerHTML = itemTitle;
        hiddenDivs.appendChild(imgTitleDiv);

        const imgImageLinkDiv = document.createElement('div');
        imgImageLinkDiv.id = 'img-image_link' + itemId;
        imgImageLinkDiv.innerHTML = itemImage;
        hiddenDivs.appendChild(imgImageLinkDiv);

        const imgProjectIdDiv = document.createElement('div');
        imgProjectIdDiv.id = 'img-project_id' + itemId;
        imgProjectIdDiv.innerHTML = itemProject;
        hiddenDivs.appendChild(imgProjectIdDiv);

        imageCard.appendChild(imageInfoDi);
        imageCard.appendChild(hiddenDivs);


        parentCol.appendChild(imageCard);
        loaderRow.appendChild(parentCol);
    }
}


