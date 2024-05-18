document.getElementById('uploadBtn').addEventListener('click', function(event) {
    const fileInput = document.querySelector('input[type="file"]');
    if (!fileInput || !fileInput.files.length) {
        // If no file is selected, do not show the loader and prevent form submission
        event.preventDefault();
        alert("Please select an image to upload :) ");
        return;
    }
    document.getElementById('loader').style.display = 'block';
});