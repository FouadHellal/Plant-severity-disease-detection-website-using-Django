document.addEventListener('DOMContentLoaded', function() {
    const uploadBtn = document.getElementById('uploadBtn');
    const terminalLoader = document.querySelector('.terminal-loader');

    uploadBtn.addEventListener('click', function() {
        terminalLoader.style.display = 'block';
        terminalLoader.classList.add('animate-in');
    });
});