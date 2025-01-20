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

                    const form = modalBody.querySelector("form");
                    if (form) {
                        handleFormSubmission(form, "/employees/new/");
                    }
                })
                .catch((error) => console.error("Error loading new employee form:", error));
        });
    }

    // Handle clicks on employee names (for editing)
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
                    modalBody.dataset.employeeId = employeeId; // Set employee ID in modalBody for deletion
                    modal.style.display = "block";

                    const form = modalBody.querySelector("form");
                    if (form) {
                        handleFormSubmission(form, `/employees/${employeeId}/edit/`);
                    }

                    // Handle delete button functionality
                    const deleteButton = modalBody.querySelector("#deleteEmployeeBtn");
                    if (deleteButton) {
                        deleteButton.addEventListener("click", () => {
                            if (confirm("Are you sure you want to delete this employee?")) {
                                deleteEmployee(employeeId);
                            }
                        });
                    }
                })
                .catch((error) => console.error("Error loading edit form:", error));
        });
    });

    // Function to handle form submission
    function handleFormSubmission(form, url) {
        form.addEventListener("submit", (event) => {
            event.preventDefault();

            const formData = new FormData(form);
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            fetch(url, {
                method: "POST",
                body: formData,
                headers: {
                    "X-CSRFToken": csrfToken,
                },
            })
                .then((response) => response.json())
                .then((result) => {
                    if (result.success) {
                        alert("Operation completed successfully!");
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
                .catch((error) => console.error("Error submitting form:", error));
        });
    }

    // Function to handle employee deletion
    function deleteEmployee(employeeId) {
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        fetch(`/employees/${employeeId}/delete/`, {
            method: "POST",
            headers: {
                "X-CSRFToken": csrfToken,
            },
        })
            .then((response) => response.json())
            .then((data) => {
                if (data.success) {
                    alert("Employee deleted successfully.");
                    modal.style.display = "none";
                    location.reload(); // Refresh the page to remove the deleted employee
                } else {
                    alert("Error: " + data.error);
                }
            })
            .catch((error) => {
                console.error("Error deleting employee:", error);
                alert("An error occurred while deleting the employee.");
            });
    }
});
