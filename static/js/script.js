// ===========================================
// HDI Predictor JavaScript
// ===========================================

document.addEventListener("DOMContentLoaded", () => {

    // ==============================
    // Scroll Reveal Animation
    // ==============================

    const hiddenElements = document.querySelectorAll(
        ".hero, .predict-card, .about-card, .stat-card, .model-box, .feature-card, .contact-card"
    );

    const observer = new IntersectionObserver((entries) => {

        entries.forEach(entry => {

            if (entry.isIntersecting) {

                entry.target.classList.add("show");

            }

        });

    }, {
        threshold: 0.15
    });

    hiddenElements.forEach(el => observer.observe(el));



    // ==============================
    // Smooth Scrolling
    // ==============================

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {

        anchor.addEventListener("click", function (e) {

            e.preventDefault();

            const target = document.querySelector(this.getAttribute("href"));

            if (target) {

                target.scrollIntoView({
                    behavior: "smooth"
                });

            }

        });

    });



    // ==============================
    // Navbar Scroll Effect
    // ==============================

    const navbar = document.querySelector("nav");

    window.addEventListener("scroll", () => {

        if (window.scrollY > 80) {

            navbar.style.background = "rgba(5,20,60,0.95)";
            navbar.style.boxShadow = "0 10px 25px rgba(0,0,0,.35)";

        }

        else {

            navbar.style.background = "rgba(0,0,0,.25)";
            navbar.style.boxShadow = "none";

        }

    });



    // ==============================
    // Button Ripple Effect
    // ==============================

    const buttons = document.querySelectorAll("button");

    buttons.forEach(button => {

        button.addEventListener("click", function (e) {

            const circle = document.createElement("span");

            const diameter = Math.max(button.clientWidth, button.clientHeight);

            const radius = diameter / 2;

            circle.style.width = circle.style.height = `${diameter}px`;

            circle.style.left =
                `${e.clientX - button.getBoundingClientRect().left - radius}px`;

            circle.style.top =
                `${e.clientY - button.getBoundingClientRect().top - radius}px`;

            circle.classList.add("ripple");

            const ripple = button.querySelector(".ripple");

            if (ripple) {

                ripple.remove();

            }

            button.appendChild(circle);

        });

    });



    // ==============================
    // Counter Animation
    // ==============================

    const counters = document.querySelectorAll(".counter");

    counters.forEach(counter => {

        const target = Number(counter.dataset.target);

        let count = 0;

        const speed = target / 100;

        function updateCounter() {

            if (count < target) {

                count += speed;

                counter.innerText = Math.ceil(count);

                requestAnimationFrame(updateCounter);

            }

            else {

                counter.innerText = target;

            }

        }

        updateCounter();

    });



    // ==============================
    // Input Focus Animation
    // ==============================

    const inputs = document.querySelectorAll("input");

    inputs.forEach(input => {

        input.addEventListener("focus", () => {

            input.style.transform = "scale(1.02)";

        });

        input.addEventListener("blur", () => {

            input.style.transform = "scale(1)";

        });

    });



    // ==============================
    // Floating Hero Icon
    // ==============================

    const circle = document.querySelector(".circle");

    if (circle) {

        let angle = 0;

        setInterval(() => {

            angle += 0.3;

            circle.style.transform =
                `translateY(${Math.sin(angle) * 10}px)`;

        }, 20);

    }



    // ==============================
    // Card Hover Animation
    // ==============================

    const cards = document.querySelectorAll(
        ".about-card, .stat-card, .model-box, .feature-card, .contact-card"
    );

    cards.forEach(card => {

        card.addEventListener("mouseenter", () => {

            card.style.transform = "translateY(-12px)";

        });

        card.addEventListener("mouseleave", () => {

            card.style.transform = "translateY(0px)";

        });

    });

});