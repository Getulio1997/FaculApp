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

// navbar

var menuHolder = document.getElementById('menuHolder')
var siteBrand = document.getElementById('siteBrand')
function menuToggle(){
  if(menuHolder.className === "drawMenu") menuHolder.className = ""
  else menuHolder.className = "drawMenu"
}
if(window.innerWidth < 426) siteBrand.innerHTML = "MAS"
window.onresize = function(){
  if(window.innerWidth < 420) siteBrand.innerHTML = "MAS"
  else siteBrand.innerHTML = "MY AWESOME WEBSITE"
}