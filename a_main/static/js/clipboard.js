function copyToClipboard(elemntID) {
	// Get the input field
	var copyInput = document.getElementById(elemntID);

	// Select the text in the input field
	copyInput.select();

	// Copy the selected text to the clipboard
	copyInput.setSelectionRange(0, 99999); // For mobile devices

	// Copy the text inside the text field
	navigator.clipboard.writeText(copyInput.value);

	// Optionally, provide some feedback to the user
	alert("URL copied to clipboard: " + copyInput.value);
}