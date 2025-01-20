from django.test import TestCase, Client
from django.urls import reverse
from .models import Employee, Skill
from .forms import EmployeeForm
from datetime import date

class EmployeeViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.skill1 = Skill.objects.create(name="Python")
        self.skill2 = Skill.objects.create(name="Django")

        self.employee1 = Employee.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            date_of_birth=date(1990, 1, 1),
            contact_number="1234567890",
            address="123 Main St",
            city="Cityville",
            postal_code="12345",
            country="Countryland"
        )
        self.employee1.skills.add(self.skill1)

        self.employee2 = Employee.objects.create(
            first_name="Jane",
            last_name="Smith",
            email="jane.smith@example.com",
            date_of_birth=date(1985, 5, 15),
            contact_number="9876543210",
            address="456 Elm St",
            city="Townsville",
            postal_code="54321",
            country="Countryland"
        )
        self.employee2.skills.add(self.skill2)

    def test_employee_list_view_get(self):
        response = self.client.get(reverse('employee_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'employees/employee_list.html')
        self.assertIn('employees', response.context)
        self.assertEqual(response.context['employees'].count(), 2)

    def test_employee_list_view_search(self):
        response = self.client.get(reverse('employee_list'), {'search': 'John'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['employees'].count(), 1)
        self.assertEqual(response.context['employees'][0].first_name, 'John')

    def test_employee_list_view_filter_by_year(self):
        response = self.client.get(reverse('employee_list'), {'filter': 'year_1990'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['employees'].count(), 1)
        self.assertEqual(response.context['employees'][0].date_of_birth.year, 1990)

    def test_employee_list_view_filter_by_skill(self):
        response = self.client.get(reverse('employee_list'), {'filter': f'skill_{self.skill1.id}'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['employees'].count(), 1)
        self.assertEqual(response.context['employees'][0].skills.first(), self.skill1)

    def test_employee_list_view_post_valid(self):
        form_data = {
            'first_name': 'Alice',
            'last_name': 'Brown',
            'email': 'alice.brown@example.com',
            'date_of_birth': '1992-07-20',
            'contact_number': '5555555555',
            'address': '789 Maple St',
            'city': 'Metropolis',
            'postal_code': '67890',
            'country': 'Countryland',
        }
        response = self.client.post(reverse('employee_list'), form_data)
        self.assertEqual(response.status_code, 302)  # Redirect on success
        self.assertEqual(Employee.objects.count(), 3)

    def test_employee_list_view_post_invalid(self):
        form_data = {
            'first_name': '',
            'last_name': 'Brown',
            'email': 'alice.brown@example.com',
            'date_of_birth': '1992-07-20',
            'contact_number': '5555555555',
            'address': '789 Maple St',
            'city': 'Metropolis',
            'postal_code': '67890',
            'country': 'Countryland',
        }
        response = self.client.post(reverse('employee_list'), form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'employees/employee_list.html')
        self.assertEqual(Employee.objects.count(), 2)

    def test_new_employee_view_post_valid(self):
        form_data = {
            'first_name': 'Charlie',
            'last_name': 'Davis',
            'email': 'charlie.davis@example.com',
            'date_of_birth': '1995-10-10',
            'contact_number': '1111111111',
            'address': '101 Birch St',
            'city': 'Capital City',
            'postal_code': '12345',
            'country': 'Countryland',
        }
        response = self.client.post(reverse('new_employee'), form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Employee.objects.count(), 3)

    def test_employee_list_view_search_no_results(self):
        response = self.client.get(reverse('employee_list'), {'search': 'NonExistent'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['employees'].count(), 0)

