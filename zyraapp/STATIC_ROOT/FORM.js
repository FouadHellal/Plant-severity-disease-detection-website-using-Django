document.getElementById('uploadFormElem').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting immediately
    document.getElementById('loader').style.display = 'inline-block'; // Show the loader
    setTimeout(() => {
      event.target.submit(); // Submit the form after showing the loader
    }, 100); // Adjust the timeout as needed
  });