from django.db import models
import random
import string

def generate_employee_id():
    letters = ''.join(random.choices(string.ascii_uppercase, k=2))
    numbers = ''.join(random.choices(string.digits, k=4))
    return f"{letters}{numbers}"


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    employee_id = models.CharField(max_length=6, unique=True, default=generate_employee_id, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    skills = models.ManyToManyField(Skill, through='EmployeeSkill')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class EmployeeSkill(models.Model):
    YRS_EXP_CHOICES = [
        ('1', '1 Year'),
        ('2', '2 Years'),
        ('3', '3 Years'),
        ('4', '4 Years'),
        ('5+', '5+ Years'),
    ]

    SENIORITY_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Expert', 'Expert'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    years_experience = models.CharField(max_length=3, choices=YRS_EXP_CHOICES)
    seniority_rating = models.CharField(max_length=12, choices=SENIORITY_CHOICES)

    def __str__(self):
        return f"{self.employee} - {self.skill}"