// Modal functionality
const modal = document.getElementById("employeeModal");
const openModalBtn = document.getElementById("newEmployeeBtn");
const closeModalBtn = document.getElementById("closeModal");

openModalBtn.onclick = function () {
    modal.style.display = "block";
};

closeModalBtn.onclick = function () {
    modal.style.display = "none";
};

window.onclick = function (event) {
    if (event.target === modal) {
        modal.style.display = "none";
    }
};

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
            <option value="4">4 Years</option>
            <option value="5+">5+ Years</option>
        </select>
        <select name="seniority_rating" required>
            <option value="Beginner">Beginner</option>
            <option value="Intermediate">Intermediate</option>
            <option value="Expert">Expert</option>
        </select>
        <button type="button" class="remove-skill">Remove</button>
    `;
    skillsContainer.appendChild(skillRow);

    // Attach remove functionality to the new skill row
    skillRow.querySelector(".remove-skill").onclick = function () {
        skillsContainer.removeChild(skillRow);
    };
};