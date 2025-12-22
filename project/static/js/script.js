// Mobile Menu Toggle
const mobileMenuBtn = document.getElementById("mobileMenuBtn")
const nav = document.getElementById("nav")

if (mobileMenuBtn && nav) {
  mobileMenuBtn.addEventListener("click", () => {
    nav.classList.toggle("active")
  })

  // Close menu when clicking outside
  document.addEventListener("click", (e) => {
    if (!nav.contains(e.target) && !mobileMenuBtn.contains(e.target)) {
      nav.classList.remove("active")
    }
  })
}

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault()
    const target = document.querySelector(this.getAttribute("href"))
    if (target) {
      target.scrollIntoView({
        behavior: "smooth",
        block: "start",
      })
    }
  })
})

// Search functionality (placeholder)
const searchInput = document.querySelector(".search-box input")
if (searchInput) {
  searchInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
      const query = e.target.value
      if (query.trim()) {
        alert("Qidiruv funksiyasi tez orada qo'shiladi: " + query)
      }
    }
  })
}

// Subscribe form handler
const subscribeForm = document.querySelector(".subscribe-form")
if (subscribeForm) {
  subscribeForm.addEventListener("submit", (e) => {
    e.preventDefault()
    const emailInput = subscribeForm.querySelector('input[type="email"]')
    if (emailInput && emailInput.value) {
      alert("Obuna bo'lganingiz uchun rahmat! Email: " + emailInput.value)
      emailInput.value = ""
    }
  })
}

// Lazy loading for images
if ("IntersectionObserver" in window) {
  const imageObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const img = entry.target
        if (img.dataset.src) {
          img.src = img.dataset.src
          img.removeAttribute("data-src")
          observer.unobserve(img)
        }
      }
    })
  })

  document.querySelectorAll("img[data-src]").forEach((img) => {
    imageObserver.observe(img)
  })
}

// Add reading progress bar for article pages
if (document.querySelector(".article-page")) {
  const progressBar = document.createElement("div")
  progressBar.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        height: 3px;
        background: #0066cc;
        width: 0%;
        z-index: 9999;
        transition: width 0.1s ease;
    `
  document.body.appendChild(progressBar)

  window.addEventListener("scroll", () => {
    const windowHeight = window.innerHeight
    const documentHeight = document.documentElement.scrollHeight - windowHeight
    const scrolled = window.scrollY
    const progress = (scrolled / documentHeight) * 100
    progressBar.style.width = progress + "%"
  })
}

// Dynamic date updates
document.querySelectorAll(".date, .widget-date, .article-date").forEach((dateElement) => {
  const dateText = dateElement.textContent
  // This is a placeholder - in a real application, you would format dates dynamically
})
