const sidebar = document.querySelector(".sidebar");
const menuBtn = document.querySelector(".menu-button");
const swLinks = document.querySelectorAll(".sw");
const username = document.getElementById("user");
const usernamePanel = document.getElementById("user-panel");
const emailPanel = document.getElementById("email-panel");

let currentCity;
if (localStorage.getItem("currentCity")) {
  currentCity = localStorage.getItem("currentCity");
} else {
  currentCity = 1;
  localStorage.setItem("currentCity", currentCity);
}

axios
  .get("http://localhost:8000/api/v1/auth/users/me", { withCredentials: true })
  .then((responce) => {
    username.innerHTML = responce.data.username;
    usernamePanel.innerHTML = responce.data.username;
    emailPanel.innerHTML = responce.data.email;
  })
  .catch((error) => {
    console.error(error);
  });

// Sidebar
menuBtn.addEventListener("click", () => {
  sidebar.classList.toggle("active");
});

swLinks.forEach((link) => {
  link.addEventListener("click", () => {
    swLinks.forEach((l) => l.classList.remove("active"));
    link.classList.add("active");
  });
});

// Topbar
document.querySelectorAll(".sw").forEach((sw) => {
  sw.addEventListener("click", (e) => {
    e.preventDefault();
    document.querySelector(".sw.selected").classList.remove("selected");
    sw.classList.add("selected");
  });
});

// Right sidebar
const toggleRightSidebar = document.getElementById("toggleRightSidebar");
const sidebar_right = document.getElementById("sidebar-right");
const overlay = document.getElementById("overlay");
const logout = document.getElementById("exit-account");

toggleRightSidebar.addEventListener("click", () => {
  sidebar_right.classList.toggle("show");
  overlay.classList.toggle("show");
});

overlay.addEventListener("click", () => {
  sidebar_right.classList.remove("show");
  overlay.classList.remove("show");
});

logout.addEventListener("click", () => {
  axios.get("http://localhost:8000/api/v1/auth/jwt/logout", {
    withCredentials: true,
  });
  // location.reload(true);
});

// Window up
let modal = document.getElementById("myModal");
let span = document.getElementsByClassName("close")[0];
let backdrop = document.getElementById("modal-backdrop");

span.onclick = function() {
  modal.style.display = "none";
  backdrop.style.display = "none";
};

window.onclick = function(event) {
  if (event.target == modal || event.target == backdrop) {
    modal.style.display = "none";
    backdrop.style.display = "none";
  }
};
