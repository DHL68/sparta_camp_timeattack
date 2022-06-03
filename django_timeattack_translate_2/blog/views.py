from django.shortcuts import render
from .models import Category, Article

# Create your views here.
def new_view(request):
    if request.method == 'POST':

    elif request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'new.html', {'categories', categories})
