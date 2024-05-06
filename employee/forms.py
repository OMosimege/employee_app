from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'contact_number', 'email', 'date_of_birth', 
                    'street_address', 'city', 'postal_code', 'country', 'rating', 'employee_id']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['contact_number'].required = True
        self.fields['email'].required = True
        self.fields['date_of_birth'].required = True
        self.fields['street_address'].required = True
        self.fields['city'].required = True
        self.fields['postal_code'].required = True
        self.fields['country'].required = True
        self.fields['rating'].required = True

    def clean(self):
        cleaned_data = super().clean()
        
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        if not instance.employee_id:
            letters = ''.join(random.choices(string.ascii_uppercase, k=2))
            numbers = ''.join(random.choices(string.digits, k=4))
            instance.employee_id = f"{letters}{numbers}"
        if commit:
            instance.save()
        return instance