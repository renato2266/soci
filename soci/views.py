# Create your views here.

#views.py

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the SOCI index.")
