// Add this to a new file: static/js/cursor.js
document.addEventListener("DOMContentLoaded", () => {
  const cursor = document.querySelector(".custom-cursor");

  document.addEventListener("mousemove", (e) => {
    cursor.style.left = e.clientX + "px";
    cursor.style.top = e.clientY + "px";
  });

  // Add active class when clicking
  document.addEventListener("mousedown", () => {
    cursor.classList.add("active");
  });

  document.addEventListener("mouseup", () => {
    cursor.classList.remove("active");
  });

  // Add hover effect for links
  const links = document.querySelectorAll("a");
  links.forEach((link) => {
    link.addEventListener("mouseenter", () => {
      cursor.classList.add("active");
    });
    link.addEventListener("mouseleave", () => {
      cursor.classList.remove("active");
    });
  });
});
