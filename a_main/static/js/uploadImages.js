
//-------------------------------//-------------------------------//-------------------------------//
// Group DOM element selections
//-------------------------------//-------------------------------//-------------------------------//

const uploadButton = document.getElementById("uploadButton");
const loaderBar = document.getElementById('dotsLoader');
const imageUpload = document.getElementById("imageUpload");

const url = document.getElementById('url').value;
const uploadDiv = document.getElementById('uploadsection');
const uploadAnimationDiv = document.getElementById('uploadAnimation');
const loadValid = document.getElementById('validate');
const LoadBackend = document.getElementById('backend');
const fileLoader = document.getElementById('fileLoader');
const fileLoaderRow = document.getElementById('fileLoaderRow');

//-------------------------------//-------------------------------//-------------------------------//
// Function to display error message and reset UI
//-------------------------------//-------------------------------//-------------------------------//

function displayError(message) {
    alert(message);
    uploadButton.style.display = 'block';
    loaderBar.style.display = 'none';
    loadValid.style.display = 'none';
	uploadDiv.classList.remove('noshow')
	uploadAnimationDiv.classList.add('noshow');
}

//-------------------------------//-------------------------------//-------------------------------//
// Handling file upload button click
//-------------------------------//-------------------------------//-------------------------------//

uploadButton.addEventListener("click", uploadFiles);

//-------------------------------//-------------------------------//-------------------------------//
// Main code for the file uploads
//-------------------------------//-------------------------------//-------------------------------//
//On click the function will start with validating the data and sending a request to the backend for
// the cf batch upload token.
//-------------------------------//-------------------------------//-------------------------------//

async function uploadFiles(event) {

    event.preventDefault();
    const csrftoken = getCookie('csrftoken');
    const fileLimit = 100; // max items
    const imageFiles = imageUpload.files; //images
    // removes the current divs showing the upload form
	uploadDiv.classList.add('noshow')
    // starts animation for validation
    uploadAnimationDiv.classList.remove('noshow');
    uploadButton.style.display = 'none';
    loadValid.style.display = 'flex';

    if (imageFiles.length === 0) {
        // Using the displayError function for consistent error handling
        displayError("Please select at least one image file of a valid format to upload.");
        return;
    }
        // validation 
    if (imageFiles.length > fileLimit) {
        displayError(`Please select up to ${fileLimit} files.`);
        return;
    }

    for (let fileObj = 0; fileObj < imageFiles.length; fileObj++) {
        const maxSize = ((imageFiles[fileObj].size / 1024) / 1024).toFixed(4);
        const allowedFiles = /\.(png|gif|jpg|jpe?g|svg)$/i;

        if (imageFiles[fileObj].name === "item" || maxSize >= 10) {
            displayError("Please check your images, individual images can be no larger than 10Mb");
            return;
        }

        if (!allowedFiles.exec(imageFiles[fileObj].name)) {
            displayError("Only valid image types can be uploaded, PNG, GIF, JPEG, JPG, SVG");
            return;
        }
    }
    // loadbar for backend call
    loaderBar.style.display = 'flex';
    // cf_data was used as a way to id the POST request on the backend
    LoadBackend.style.display = 'flex';

    //-------------------------------//
    // bath token request
    //-------------------------------//

    try {
        // sending request to backend for batch upload token
        const responseData = await (await fetch(url, {
            method: 'GET',
            //set same origin since this is the same project
            credentials: 'same-origin',
            headers: {
                'token_request': 'token_request',
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            }
        })).json();

        loadValid.style.display = 'none';
        LoadBackend.style.display = 'none';
        // Using destructuring to get the result from uploadImages function
        const {backEndData} = await uploadImages(responseData, imageFiles);
        // redicrects to the next page and send the cf ids back for encoding
        delayedRedirect(backEndData);

    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while processing the request, please refresh and try again. If the issue persists, please contact the site admin.');
        return;
    }
}



// Function to upload images to the backend
async function uploadImages(responseData, imageFiles) {
    const backEndData = [];
    
    fileLoader.classList.remove('noshow');
    const cloudflareId = responseData[0].cf_token;
    console.log(responseData[0].cf_token)
    const cloudflareURL = responseData[0].cf_url;

    for (let fileCounter = 0; fileCounter < imageFiles.length; fileCounter++) {
        const imgMultiPart = new FormData();

        // Creating DOM elements for progress display
        const divCol = document.createElement('div');
        divCol.className = 'col-12 col-md-3 mb-1';
        fileLoaderRow.appendChild(divCol);

        const progLoader = document.createElement('div');
        progLoader.className = 'loaderFile';
        divCol.appendChild(progLoader);

        const nameLoader = document.createElement('p');
        nameLoader.className = 'p-p';
        nameLoader.innerHTML = '#' + fileCounter + ' ' + imageFiles[fileCounter].name;
        divCol.appendChild(nameLoader);

        imgMultiPart.append("file", imageFiles[fileCounter]);
        var metadata = { "silk_id": "STJH" };
        imgMultiPart.append('metadata', JSON.stringify(metadata));
        //-------------------------------//
        // for loop image direct upload 
        //-------------------------------//

        try {
            const response = await fetch(cloudflareURL, {
                method: "post",
                body: imgMultiPart,
                headers: {
                    'authorization': `Bearer ${cloudflareId}`
                },
            });

            if (!response.ok) {
                // Check if the response status is not OK (HTTP 2xx)
                console.error(`Request failed with status: ${response.status}`);
                progLoader.classList.remove('loaderFile');
                progLoader.classList.add('loadedFailed');
                
            }

            // If the response is OK, show image bar uploaded
            const cf_resp = await response.json(); 
            console.log(cf_resp.result.id);
            progLoader.classList.remove('loaderFile');
            progLoader.classList.add('loadedFile');
            backEndData.push(cf_resp.result.id);

            fileLoader.scrollIntoView({ behavior: 'smooth', block: 'end' });
        } catch (error) {
            console.error("Error in fetch:", error);
            progLoader.classList.remove('loaderFile');
            progLoader.classList.add('loadedFailed');
            
        }
    }
    // after the files are uploaded the list of cf ids are returned 
    return { 'backEndData': backEndData};
}


// Function to handle delayed redirect
function delayedRedirect(backEndData) {
    const csrfGet = getCookie('csrftoken');
    const data = { 'data': backEndData};
    //-------------------------------//
    // redirect request with cf IDs 
    //-------------------------------//
    fetch(url, {
        method: 'POST',
        body: JSON.stringify(data),
        credentials: 'same-origin',
        headers: {
            'cf_data': 'cf_data',
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfGet
        }
    })
    .then(response => response.text())
    .then(response => {
        const newURL = response.slice(1, -1);
        window.location.href = newURL;
    })
    .catch(error => console.error('Error:', error));
}
