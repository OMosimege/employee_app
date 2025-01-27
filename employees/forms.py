from django import forms
from django.core.exceptions import ValidationError
from datetime import date
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
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not self.instance.pk:  # This means the form is for a new employee
            if Employee.objects.filter(email=email).exists():
                raise ValidationError("An employee with this email address already exists.")
        else:  # This means the form is for an existing employee (edit)
            # Check if the email belongs to a different employee
            if Employee.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
                raise ValidationError("An employee with this email address already exists.")
        return email

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if date_of_birth >= date.today():
            raise forms.ValidationError("The date of birth must be in the past.")
        return date_of_birth
