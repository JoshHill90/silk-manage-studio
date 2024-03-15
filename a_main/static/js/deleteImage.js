//-------------------------------//-------------------------------//-------------------------------//
// Group DOM element selections
//-------------------------------//-------------------------------//-------------------------------//
const deleteURL = document.getElementById('deleteURL').value
const deletButton = document.getElementById('delete')
const batchURL = document.getElementById('cf_batch_url').value

//-------------------------------//-------------------------------//-------------------------------//
// - Event for Delete click
// the fuctions calls a request to the backend for a 
// token to prform the action and the ID for the images 
//-------------------------------//-------------------------------//-------------------------------//



deletButton.addEventListener('click', (clicked) => {
    clicked.preventDefault();
	imageArray = []
    
	const ElemtSet = document.getElementsByClassName('image-card-a')
    const selectedCard = Array.from(ElemtSet);

    for (let set = 0; set < selectedCard.length; ++set) {
        console.log(selectedCard[set].id, set,  ElemtSet.length, 'check')
        imageArray.push(selectedCard[set].id)
		selectedCard[set].parentNode.remove()
	}
    console.log(imageArray)
    const csrfGet = getCookie('csrftoken');
    const data = { 'data': imageArray};
    //-------------------------------//
    // redirect request with cf IDs 
    //-------------------------------//
    fetch(deleteURL, {
        method: 'POST',
        body: JSON.stringify(data),
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfGet
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Backend Error: ${response.status}, please refush and try again.`);
        }
    })
    .catch(error => {
        alert(error, ' please refesh and rety')
        return false
    });
});