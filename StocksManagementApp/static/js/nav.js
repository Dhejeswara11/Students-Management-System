document.addEventListener("DOMContentLoaded", function () {
    // Navbar Toggler
    const navbarToggler = document.querySelector(".navbar-toggler");
    const navbarCollapse = document.querySelector(".navbar-collapse");
    
    if (navbarToggler && navbarCollapse) {
        navbarToggler.addEventListener("click", function () {
            navbarCollapse.classList.toggle("show");
        });
    }

    // Close navbar on clicking outside (for mobile screens)
    document.addEventListener("click", function (event) {
        if (!navbarToggler.contains(event.target) && !navbarCollapse.contains(event.target)) {
            navbarCollapse.classList.remove("show");
        }
    });

    // Dropdown menu handling
    const dropdowns = document.querySelectorAll(".nav-item.dropdown");
    dropdowns.forEach(dropdown => {
        dropdown.addEventListener("mouseenter", function () {
            if (window.innerWidth > 992) {
                this.querySelector(".dropdown-menu").classList.add("show");
            }
        });
        dropdown.addEventListener("mouseleave", function () {
            if (window.innerWidth > 992) {
                this.querySelector(".dropdown-menu").classList.remove("show");
            }
        });
    });
});
