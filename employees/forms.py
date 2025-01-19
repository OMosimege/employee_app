from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'first_name',
            'last_name',
            'contact_number',
            'email',
            'date_of_birth',
            'address',
            'city',
            'postal_code',
            'country',
            'skills'
        ]