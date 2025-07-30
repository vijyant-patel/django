from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from .forms import ZipUploadForm
from .models import ZipFileUpload
from django.conf import settings
import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

class ZipView(LoginRequiredMixin, generic.ListView):
    template_name = 'myzipapp/list.html'
    context_object_name = 'zips'

    def get_queryset(self):
        return ZipFileUpload.objects.all()


@login_required
def list_zips(request):
    zips = ZipFileUpload.objects.all().order_by('-uploaded_at')
    return render(request, 'myzipapp/list.html', {'zips': zips})

def upload_zip(request):
    if request.method == 'POST':
        form = ZipUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_zips')
    else:
        form = ZipUploadForm()
    return render(request, 'myzipapp/upload.html', {'form': form})

def download_zip(request, pk):
    zip_file = ZipFileUpload.objects.get(pk=pk)
    file_path = zip_file.file.path
    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=os.path.basename(file_path))
