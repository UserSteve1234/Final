from django.shortcuts import render, redirect
from .models import Publications
from .forms import SocialForm
from django.contrib.auth.models import User

# Create your views here.
admin = User.objects.get(id=1)


def publications_view(request):
    context = {
        "title": "Publications",
        "publications": Publications.objects.all(),
    }
    return render(request, 'main.html', context)


def create_publication_view(request):
    form = SocialForm()
    if request.method == 'POST':
        form = SocialForm(request.POST, request.FILES)  # Обрабатываем файлы
        if form.is_valid():
            form.instance.author_of_publication = admin
            form.save()
            return redirect('publications_view')
    return render(request, 'create_public.html', {'form': form})


def update_publication_view(request, pk):
    publication = Publications.objects.get(pk=pk)
    if request.method == 'POST':
        form = SocialForm(request.POST, request.FILES, instance=publication)
        if form.is_valid():
            if form.cleaned_data.get('delete_image'):
                # Удаляет файл изображения
                publication.image.delete(save=False)
                publication.image = None  # Удаляет ссылку на изображение в модели
            form.save()
            return redirect('publications_view')
    else:
        form = SocialForm(instance=publication)
    return render(request, 'update_public.html', {'form': form})


def delete_publication_view(request, pk):
    publication = Publications.objects.get(pk=pk)
    if request.method == 'POST':
        publication.delete()
        return redirect('publications_view')
    return render(request, 'delete_public.html', {'publication': publication})
