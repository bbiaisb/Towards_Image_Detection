from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import DocumentForm

from django.conf import settings
from django.core.files.storage import FileSystemStorage

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "Hello there.",
        "my_number": 123,
        "my_list": [1, 2, 3, 4, 5]
    }
    return render(request, "about.html", my_context)

def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Contact Page</h1>")
