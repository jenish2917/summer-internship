from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def students(request):
    student = [
        {'id': 1, 'name': 'John', 'age': 20},
    ]
    return HttpResponse(student)
