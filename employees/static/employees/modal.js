document.addEventListener("DOMContentLoaded", function () {
    const modal = document.getElementById("employeeModal");
    const modalBody = document.getElementById("modalBody");
    const closeModalBtn = document.getElementById("closeModal");
    const newEmployeeBtn = document.getElementById("newEmployeeBtn");

    // Close modal functionality
    closeModalBtn.addEventListener("click", () => {
        modal.style.display = "none";
        modalBody.innerHTML = ""; // Clear modal content
    });

    // Handle the "+ New Employee" button
    if (newEmployeeBtn) {
        newEmployeeBtn.addEventListener("click", () => {
            fetch(`/employees/new/`) // Adjust this URL if needed
                .then((response) => response.text())
                .then((html) => {
                    modalBody.innerHTML = html; // Populate modal with form
                    modal.style.display = "block";

                    // Add form submission handling
                    const form = modalBody.querySelector("form");
                    if (form) {
                        form.addEventListener("submit", (event) => {
                            event.preventDefault();

                            const formData = new FormData(form);
                            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

                            fetch(`/employees/new/`, {
                                method: "POST",
                                body: formData,
                                headers: {
                                    "X-CSRFToken": csrfToken,
                                },
                            })
                                .then((response) => response.json())
                                .then((result) => {
                                    if (result.success) {
                                        alert("New employee added successfully!");
                                        modal.style.display = "none";
                                        location.reload(); // Reload the page to reflect changes
                                    } else {
                                        // Handle validation errors
                                        const errorLists = modalBody.querySelectorAll(".errorlist");
                                        errorLists.forEach((list) => list.remove());

                                        for (const [field, errors] of Object.entries(result.errors)) {
                                            const fieldElement = modalBody.querySelector(`[name="${field}"]`);
                                            if (fieldElement) {
                                                const errorList = document.createElement("ul");
                                                errorList.classList.add("errorlist");
                                                errors.forEach((error) => {
                                                    const errorItem = document.createElement("li");
                                                    errorItem.textContent = error;
                                                    errorList.appendChild(errorItem);
                                                });
                                                fieldElement.parentNode.appendChild(errorList);
                                            }
                                        }
                                    }
                                })
                                .catch((error) => console.error("Error adding new employee:", error));
                        });
                    }
                })
                .catch((error) => console.error("Error loading new employee form:", error));
        });
    }

    // Handle clicks on employee names (already defined for edit)
    const employeeLinks = document.querySelectorAll('.employee-card p .employee-name');

    employeeLinks.forEach((link) => {
        link.addEventListener('click', function (event) {
            event.preventDefault();

            const employeeId = this.dataset.id; // Get employee ID
            if (!employeeId) {
                console.error("Employee ID is undefined.");
                return;
            }

            // Fetch the edit_employee.html form
            fetch(`/employees/${employeeId}/edit/`)
                .then((response) => response.text())
                .then((html) => {
                    modalBody.innerHTML = html; // Populate modal with form
                    modal.style.display = "block";

                    // Add form submission handling
                    const form = modalBody.querySelector("form");
                    if (form) {
                        form.addEventListener("submit", (event) => {
                            event.preventDefault();

                            const formData = new FormData(form);
                            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

                            fetch(`/employees/${employeeId}/edit/`, {
                                method: "POST",
                                body: formData,
                                headers: {
                                    "X-CSRFToken": csrfToken,
                                },
                            })
                                .then((response) => response.json())
                                .then((result) => {
                                    if (result.success) {
                                        alert("Employee updated successfully!");
                                        modal.style.display = "none";
                                        location.reload(); // Reload the page to reflect changes
                                    } else {
                                        // Handle validation errors
                                        const errorLists = modalBody.querySelectorAll(".errorlist");
                                        errorLists.forEach((list) => list.remove());

                                        for (const [field, errors] of Object.entries(result.errors)) {
                                            const fieldElement = modalBody.querySelector(`[name="${field}"]`);
                                            if (fieldElement) {
                                                const errorList = document.createElement("ul");
                                                errorList.classList.add("errorlist");
                                                errors.forEach((error) => {
                                                    const errorItem = document.createElement("li");
                                                    errorItem.textContent = error;
                                                    errorList.appendChild(errorItem);
                                                });
                                                fieldElement.parentNode.appendChild(errorList);
                                            }
                                        }
                                    }
                                })
                                .catch((error) => console.error("Error saving changes:", error));
                        });
                    }
                })
                .catch((error) => console.error("Error loading edit form:", error));
        });
    });
});
