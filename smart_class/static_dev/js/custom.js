document.addEventListener("DOMContentLoaded", () => {
  const themeToggleButtons = document.querySelectorAll("[data-bs-theme-value]");
  const body = document.body;

  themeToggleButtons.forEach(button => {
    button.addEventListener("click", () => {
      const themeValue = button.getAttribute("data-bs-theme-value");
      body.setAttribute("data-bs-theme", themeValue);
      localStorage.setItem("theme", themeValue);
    });
  });

  const savedTheme = localStorage.getItem("theme") || "light";
  body.setAttribute("data-bs-theme", savedTheme);

  const logo = document.querySelector(".logo");
  const navMenu = document.querySelector("#main-nav");

  if (logo && navMenu) {
    logo.addEventListener("click", (event) => {
      event.preventDefault();
      if (navMenu.classList.contains("show")) {
        navMenu.classList.remove("show");
      } else {
        document.querySelectorAll(".dropdown-menu.show").forEach(menu => menu.classList.remove("show"));
        navMenu.classList.add("show");
      }
    });
  }

  document.addEventListener("click", (event) => {
    if (!navMenu.contains(event.target) && !logo.contains(event.target)) {
      navMenu.classList.remove("show");
    }
  });
});