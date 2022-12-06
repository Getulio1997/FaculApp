const chk = document.querySelector('#chk')

function toggleDarkMode() {
  document.body.classList.toggle("dark");
}

function loadTheme() {
  const darkMode = localStorage.getItem("dark");
  
  if (darkMode) {
    toggleDarkMode();
  }
}

loadTheme();

chk.addEventListener('change', function () {
  toggleDarkMode()

  localStorage.removeItem("dark");
  
  if (document.body.classList.contains("dark")) {
    localStorage.setItem ("dark", 1);
  }
});