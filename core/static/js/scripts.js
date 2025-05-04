document.addEventListener("DOMContentLoaded", function () {
  const fadeElements = document.querySelectorAll(".fade-in");

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
      }
    });
  });

  fadeElements.forEach((element) => {
    observer.observe(element);
  });
});

//  cursor.js or create a new file
document.addEventListener("DOMContentLoaded", function () {
  // Typing effect
  const typed = new Typed("#typing-text", {
    strings: [
      "Software Developer",
      "Full Stack Engineer",
      "Problem Solver",
      "Tech Enthusiast",
      "Code Craftswoman",
      "API Developer",
      "AWS Practitioner",
      ,
    ],
    typeSpeed: 50,
    backSpeed: 30,
    backDelay: 1500,
    loop: true,
    showCursor: true,
    cursorChar: "|",
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const aboutCode = document.getElementById("about-code");
  const gladysOro = new GladysOro();

  // Convert the class instance to a formatted string
  const formattedCode = JSON.stringify(gladysOro, null, 2)
    .replace(/"([^"]+)":/g, "$1:")
    .replace(/"/g, "'");

  aboutCode.textContent = formattedCode;
});

// Project stack hover effect
document.addEventListener("DOMContentLoaded", function () {
  const projectStacks = document.querySelectorAll(".project-stack");

  projectStacks.forEach((stack) => {
    stack.addEventListener("mousemove", (e) => {
      const rect = stack.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;

      const centerX = rect.width / 2;
      const centerY = rect.height / 2;

      const angleX = (y - centerY) / 20;
      const angleY = (centerX - x) / 20;

      stack.style.transform = `perspective(1000px) rotateX(${angleX}deg) rotateY(${angleY}deg)`;
    });

    stack.addEventListener("mouseleave", () => {
      stack.style.transform = "perspective(1000px) rotateX(0) rotateY(0)";
    });
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const contactBtn = document.getElementById("contact-btn");
  const contactForm = document.getElementById("contact-form");

  if (contactBtn && contactForm) {
    contactBtn.addEventListener("click", function () {
      if (contactForm.classList.contains("contact-form-hidden")) {
        contactForm.classList.remove("contact-form-hidden");
        contactForm.classList.add("contact-form-visible");
        contactForm.scrollIntoView({ behavior: "smooth", block: "start" });
      } else {
        contactForm.classList.remove("contact-form-visible");
        contactForm.classList.add("contact-form-hidden");
      }
    });
  }

  // Form submission handling
  const form = document.querySelector(".form-container");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      // Add your form submission logic here
      alert("Form would submit here in a real implementation");
      this.reset();
      contactForm.classList.add("contact-form-hidden");
    });
  }
});
