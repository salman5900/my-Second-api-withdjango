from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def student_web(request):
    return HttpResponse("List of students will be displayed here.")
