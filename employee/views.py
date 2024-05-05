from django.shortcuts import render

def home(request):
    template = "employee/home.html"
    context = {}

    return render(request, template_name=template, context=context)
