// main.js

// Typing animation (optional)
document.addEventListener("DOMContentLoaded", () => {
  const typedText = document.getElementById("typed-text");
  if (typedText) {
    const text = "Developer | Problem Solver | Tech Enthusiast";
    let index = 0;

    function typeNextChar() {
      if (index < text.length) {
        typedText.textContent += text.charAt(index);
        index++;
        setTimeout(typeNextChar, 100);
      }
    }

    typedText.textContent = "";
    typeNextChar();
  }

  // Lottie animation for order confirmation
  const successContainer = document.getElementById("success-animation");
  if (successContainer) {
    lottie.loadAnimation({
      container: successContainer,
      renderer: "svg",
      loop: false,
      autoplay: true,
      path: "/app/static/assests/animations/success-animation.json"
    });
  }

  // Theme toggle (if you add one later)
  const toggle = document.getElementById("theme-toggle");
  const icon = document.getElementById("toggle-icon");

  if (toggle && icon) {
    toggle.addEventListener("click", () => {
      document.body.classList.toggle("dark-mode");
      document.body.classList.toggle("light-mode");
      icon.textContent = document.body.classList.contains("dark-mode") ? "☀️" : "🌙";
    });
  }
});

document.addEventListener("DOMContentLoaded", () => {
  const successContainer = document.getElementById("success-animation");
  if (successContainer) {
    lottie.loadAnimation({
      container: successContainer,
      renderer: "svg",
      loop: false,
      autoplay: true,
      path: "/app/static/assests/animations/success-animation.json"
    });
  }
});

const heroAnim = document.getElementById("hero-animation");
if (heroAnim) {
  lottie.loadAnimation({
    container: heroAnim,
    renderer: "svg",
    loop: true,
    autoplay: true,
    path: "/static/assets/animations/shopping-bag.json" // Replace with your actual file
  });
}

document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.getElementById("theme-toggle");
  const icon = document.getElementById("toggle-icon");

  if (toggle && icon) {
    toggle.addEventListener("click", () => {
      document.body.classList.toggle("dark-mode");
      const isDark = document.body.classList.contains("dark-mode");
      icon.textContent = isDark ? "☀️" : "🌙";
    });
  }
});

// === Scroll-triggered animation for product cards ===
const cards = document.querySelectorAll('.product-card');

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, {
  threshold: 0.1
});

cards.forEach(card => {
  observer.observe(card);
});

// === GSAP bounce effect on buttons ===
gsap.utils.toArray("button, .checkout-btn, .login-btn").forEach(btn => {
  btn.addEventListener("mouseenter", () => {
    gsap.fromTo(btn, { scale: 1 }, { scale: 1.1, duration: 0.2, ease: "back.out(2)" });
  });
  btn.addEventListener("mouseleave", () => {
    gsap.to(btn, { scale: 1, duration: 0.2, ease: "back.in(1.7)" });
  });
});

// === Optional: Confetti background ===
const canvas = document.getElementById("confetti");
if (canvas) {
  const ctx = canvas.getContext("2d");
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;

  const confetti = Array.from({ length: 100 }, () => ({
    x: Math.random() * canvas.width,
    y: Math.random() * canvas.height,
    r: Math.random() * 6 + 4,
    d: Math.random() * 50 + 10,
    color: `hsl(${Math.random() * 360}, 100%, 70%)`,
    tilt: Math.random() * 10 - 10,
    tiltAngle: 0,
    tiltAngleIncrement: Math.random() * 0.07 + 0.05
  }));

  function drawConfetti() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    confetti.forEach(c => {
      ctx.beginPath();
      ctx.lineWidth = c.r / 2;
      ctx.strokeStyle = c.color;
      ctx.moveTo(c.x + c.tilt + c.r / 2, c.y);
      ctx.lineTo(c.x + c.tilt, c.y + c.tilt + c.r / 2);
      ctx.stroke();
    });
    updateConfetti();
    requestAnimationFrame(drawConfetti);
  }

  function updateConfetti() {
    confetti.forEach(c => {
      c.y += Math.cos(c.d) + 1 + c.r / 2;
      c.x += Math.sin(c.d);
      c.tiltAngle += c.tiltAngleIncrement;
      c.tilt = Math.sin(c.tiltAngle) * 15;

      if (c.y > canvas.height) {
        c.y = -10;
        c.x = Math.random() * canvas.width;
      }
    });
  }

  drawConfetti();
}

const themeToggle = document.getElementById("theme-toggle");
themeToggle?.addEventListener("click", () => {
  document.body.classList.toggle("dark-mode");
  localStorage.setItem("theme", document.body.classList.contains("dark-mode") ? "dark" : "light");
});

// Load saved theme
if (localStorage.getItem("theme") === "dark") {
  document.body.classList.add("dark-mode");
}

document.addEventListener("DOMContentLoaded", () => {
  const toggleBtn = document.getElementById("toggle-categories");
  const categoryMenu = document.getElementById("category-menu");

  if (toggleBtn && categoryMenu) {
    toggleBtn.addEventListener("click", () => {
      categoryMenu.classList.toggle("show");
    });
  }
});

document.addEventListener("DOMContentLoaded", () => {
  const toggleBtn = document.getElementById("toggle-categories");
  const categoryMenu = document.getElementById("category-menu");
  const themeToggle = document.getElementById("theme-toggle");

  if (toggleBtn && categoryMenu) {
    toggleBtn.addEventListener("click", () => {
      categoryMenu.classList.toggle("show");
    });
  }

  if (themeToggle) {
    themeToggle.addEventListener("click", () => {
      document.body.classList.toggle("dark-mode");
      themeToggle.textContent = document.body.classList.contains("dark-mode") ? "☀️" : "🌙";
    });
  }
});

let currentSlide = 0;
const slides = document.querySelectorAll('.carousel-slide');

function changeSlide(direction) {
  slides[currentSlide].classList.remove('active');
  currentSlide = (currentSlide + direction + slides.length) % slides.length;
  slides[currentSlide].classList.add('active');
}
