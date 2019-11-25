from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Image
from .forms import ImageForm

from django.conf import settings
from django.core.files.storage import FileSystemStorage


def model_form_upload(request, *args, **kwargs):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('../step2/')
    else:
        form = DocumentForm()
    return render(request, 'step1.html', {
        'form': form
    })


def model_image_edit(request, *args, **kwargs):

    lastimage = Image.objects.last()

    if lastimage != None:
        imagefile = lastimage.imagefile
    else:
        imagefile = 'images/image_1.png'

    form = ImageForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()

    context = {'imagefile': imagefile,
               'form': form
               }

    print(context)

    return render(request, "step2.html", context)

# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

