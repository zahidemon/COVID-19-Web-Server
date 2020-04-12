from django.shortcuts import render
from .forms import UploadForm
import numpy as np
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from django.core.files.storage import default_storage
from django.contrib import messages
# Create your views here.

def index(request):
    context = {}
    if request.method == "POST":
        f = request.FILES['sentFile'] # here you get the files needed
        if not (f.name.endswith('.jpg') or f.name.endswith('.jpeg') or f.name.endswith('.JPEG') or f.name.endswith('.png') or f.name.endswith('.JPG')):
            messages.error(request,'This format is not supported.')
            return render(request,'index.html')
        response = {}
        file_name = "pic.jpg"
        file_name_2 = default_storage.save(file_name, f)
        file_url = default_storage.url(file_name_2)
        original = load_img(file_url, target_size=(224, 224))
        numpy_image = img_to_array(original)
        print(numpy_image.shape)

        

    return render(request, "index.html")


def Model(request):
    return render(request,'model.html')


def About(request):
    return render(request,'about.html')
