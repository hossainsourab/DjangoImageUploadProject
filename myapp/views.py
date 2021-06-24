from django.shortcuts import render
from .models import Image
from .forms import ImageForm


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ImageForm()

    img = Image.objects.all()
    dicts = {'title': 'Home | Image Upload', 'form': form, 'img': img}
    return render(request, 'myapp/home.html', context=dicts)
