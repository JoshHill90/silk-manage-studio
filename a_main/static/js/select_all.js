//-------------------------------//-------------------------------//-------------------------------//
// Group DOM element selections
//-------------------------------//-------------------------------//-------------------------------//
const divLoaderRow = document.getElementById('loaderRow')

//-------------------------------//-------------------------------//-------------------------------//
// Event for dynamiclly loaded images, to check them if they are active 
//-------------------------------//-------------------------------//-------------------------------//

// 
divLoaderRow.addEventListener("change", function (event) {
    // Check if the change event was triggered by a checkbox
    if (event.target.type === "checkbox") {
        var cardDiv = event.target.parentNode; // Get the parent of the checkbox
        
        if (event.target.checked) {
            cardDiv.classList.remove("image-card");
            cardDiv.classList.add("image-card-a");
        } else {
            cardDiv.classList.remove("image-card-a");
            cardDiv.classList.add("image-card");
        }
    }
});

//-------------------------------//-------------------------------//-------------------------------//
// for loop image direct upload 
//-------------------------------//-------------------------------//-------------------------------//

function toggle(source) {
    var checkboxes = document.querySelectorAll('.checkImage');
    for (var i = 0; i < checkboxes.length; i++) {
        var boxI = checkboxes[i].parentNode;
        //console.log(selectedCard)
        if (checkboxes[i] != source){
            checkboxes[i].checked = source.checked;
        };
        if (source.checked == true) {
            boxI.classList.remove("image-card");
            boxI.classList.add("image-card-a");
        } else {
            boxI.classList.remove("image-card-a");
            boxI.classList.add("image-card");
        };
    };
};
