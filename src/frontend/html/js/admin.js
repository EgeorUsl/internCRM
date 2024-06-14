const sidebar = document.querySelector(".sidebar");
const menuBtn = document.querySelector(".menu-button");
const swLinks = document.querySelectorAll('.sw');

menuBtn.addEventListener("click", () => {
  sidebar.classList.toggle("active");
});

document.querySelectorAll(".program-title").forEach((title) => {
  title.addEventListener("click", () => {
    title.classList.toggle("open");
    title.parentElement.querySelector(".group").classList.toggle("open");
  });
});

document.querySelectorAll(".group-title").forEach((title) => {
  title.addEventListener("click", () => {
    title.classList.toggle("open");
    title.parentElement
      .querySelector(".group-content")
      .classList.toggle("open");
  });
});

swLinks.forEach(link => {
  link.addEventListener('click', () => {
    swLinks.forEach(l => l.classList.remove('active'));
    link.classList.add('active');
  });
});
