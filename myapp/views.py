from django.shortcuts import render, redirect
from .forms import URLForm, UploadFileForm
from .models import URL
import requests
from django.shortcuts import render, redirect, get_object_or_404

from django.shortcuts import render, redirect
from .forms import URLForm, UploadFileForm
from .models import URL
import requests
from requests.exceptions import ConnectionError

def index(request):
    urls = URL.objects.all()

    if request.method == 'POST':
        form = URLForm(request.POST)
        upload_form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            url_str = form.cleaned_data['url']
            if not url_str.startswith('http://') and not url_str.startswith('https://'):
                url_str = 'http://' + url_str
            try:
                response = requests.get(url_str)
                status_code = response.status_code
            except ConnectionError:
                status_code = 500
            url, created = URL.objects.get_or_create(url=url_str, defaults={'status_code': status_code})
            if not created:
                url.status_code = status_code
                url.save()
            return redirect('index')

        if upload_form.is_valid():
            file = request.FILES['file']
            for line in file:
                url_str = line.decode().strip()
                if not url_str.startswith('http://') and not url_str.startswith('https://'):
                    url_str = 'http://' + url_str
                try:
                    response = requests.get(url_str)
                    status_code = response.status_code
                except ConnectionError:
                    status_code = 500
                url, created = URL.objects.get_or_create(url=url_str, defaults={'status_code': status_code})
                if not created:
                    url.status_code = status_code
                    url.save()
            return redirect('index')

    else:
        form = URLForm()
        upload_form = UploadFileForm()

    return render(request, 'index.html', {'urls': urls, 'form': form, 'upload_form': upload_form})

def delete_url(request, url_id):
    url = get_object_or_404(URL, pk=url_id)
    url.delete()
    return redirect('index')
