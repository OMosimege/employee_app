from django.test import TestCase, Client
from django.urls import reverse
from .models import Employee, Skill
from datetime import date, timedelta


class EmployeeViewTests(TestCase):
    def setUp(self):
        self.client = Client()

        self.skill = Skill.objects.create(name="Python")
        self.employee_data = {
            "first_name": "John",
            "last_name": "Doe",
            "contact_number": "1234567890",
            "email": "john.doe@example.com",
            "date_of_birth": (date.today() - timedelta(days=365 * 30)).isoformat(),
            "address": "123 Main St",
            "city": "Pretoria",
            "postal_code": "0001",
            "country": "South Africa",
        }

    def test_employee_list_view(self):
        """Test the employee_list view renders correctly."""
        response = self.client.get(reverse('employee_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'employees/employee_list.html')

    def test_create_employee_success(self):
        """Test that an employee is successfully created."""
        response = self.client.post(reverse('employee_list'), data=self.employee_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Employee.objects.count(), 1)
        self.assertEqual(Employee.objects.first().email, "john.doe@example.com")

    def test_create_employee_duplicate_email(self):
        """Test creating an employee with a duplicate email fails."""
        Employee.objects.create(**self.employee_data)
        response = self.client.post(reverse('employee_list'), data=self.employee_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "An employee with this email address already exists.")
        self.assertEqual(Employee.objects.count(), 1)

    def test_create_employee_future_date_of_birth(self):
        """Test creating an employee with a future date of birth fails."""
        invalid_data = self.employee_data.copy()
        invalid_data["date_of_birth"] = (date.today() + timedelta(days=1)).isoformat()
        response = self.client.post(reverse('employee_list'), data=invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The date of birth must be in the past.")
        self.assertEqual(Employee.objects.count(), 0)

    def test_modal_displays_validation_errors(self):
        """Test that validation errors are displayed in the modal."""
        invalid_data = self.employee_data.copy()
        invalid_data["email"] = ""
        response = self.client.post(reverse('employee_list'), data=invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This field is required.")
        self.assertEqual(Employee.objects.count(), 0)

