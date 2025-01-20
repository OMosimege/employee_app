// Modal functionality
document.addEventListener("DOMContentLoaded", () => {
    const modal = document.getElementById("employeeModal");
    const openModalBtn = document.getElementById("newEmployeeBtn");
    const closeModalBtn = document.getElementById("closeModal");
    const form = modal.querySelector("form");

    // Open the modal
    openModalBtn.addEventListener("click", () => {
        modal.style.display = "block";
    });

    // Close the modal and reset the form
    closeModalBtn.addEventListener("click", () => {
        modal.style.display = "none";
        form.reset(); // Clear all fields
    });

    // Close modal when clicking outside the modal content
    window.addEventListener("click", (event) => {
        if (event.target === modal) {
            modal.style.display = "none";
            form.reset(); // Clear all fields
        }
    });
});

// Add and remove skills dynamically
const skillsContainer = document.getElementById("skills-container");
const addSkillBtn = document.getElementById("addSkillBtn");

addSkillBtn.onclick = function () {
    const skillRow = document.createElement("div");
    skillRow.classList.add("skill-row");
    skillRow.innerHTML = `
        <input type="text" name="skill" placeholder="Skill" required>
        <select name="years_experience" required>
            <option value="1">1 Year</option>
            <option value="2">2 Years</option>
            <option value="3">3 Years</option>
            <option v
