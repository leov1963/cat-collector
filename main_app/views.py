from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

    

# 1. Make a view function
# 2. Make the html page
# 3. Add the view to the urls.py inside of main_app.urls
# In browser
# When I go to localhost:8000/contact
# Django -> urls -> /contact -> vews.contact (runs function) -> templates -> contact.html