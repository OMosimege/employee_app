from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    email = models.EmailField()
    date_of_birth = models.DateField()
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=6, unique=True, editable=False, default='TEMPID')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.employee_id or self.employee_id == 'TEMPID':
            self.employee_id = self.generate_unique_employee_id()
        super(Employee, self).save(*args, **kwargs)

    @staticmethod
    def generate_unique_employee_id():
        while True:
            letters = ''.join(random.choices(string.ascii_uppercase, k=2))
            numbers = ''.join(random.choices(string.digits, k=4))
            employee_id = f"{letters}{numbers}"
            if not Employee.objects.filter(employee_id=employee_id).exists():
                return employee_id


class Skill(models.Model):
    SENIORITY_RATING = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Expert', 'Expert'),
    )
    name = models.CharField(max_length=100)
    years_exp = models.CharField(max_length=5)
    rating = models.CharField(max_length=20, choices=SENIORITY_RATING)
    employee = models.ForeignKey(
        "Employee", on_delete=models.CASCADE, blank=True, related_name="employee"
    )

    def __str__(self):
        return self.name
