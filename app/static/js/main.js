document.addEventListener('DOMContentLoaded', (event) => {
    const toggleMode = document.querySelector('.toggle-mode');
    const modeIcon = document.querySelector('#mode-icon');
    let darkModeEnabled = localStorage.getItem('dark-mode') === 'true';

    if (darkModeEnabled) {
        enableDarkMode();
    }

    toggleMode.addEventListener('click', () => {
        darkModeEnabled = !darkModeEnabled;
        localStorage.setItem('dark-mode', darkModeEnabled);
        if (darkModeEnabled) {
            enableDarkMode();
        } else {
            disableDarkMode();
        }
    });

    function enableDarkMode() {
        document.body.classList.add('dark-mode');
        modeIcon.classList.remove('fa-moon');
        modeIcon.classList.add('fa-sun');
    }

    function disableDarkMode() {
        document.body.classList.remove('dark-mode');
        modeIcon.classList.remove('fa-sun');
        modeIcon.classList.add('fa-moon');
    }
});
