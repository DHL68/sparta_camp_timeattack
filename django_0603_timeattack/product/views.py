from django.shortcuts import render
from .models import Category, Drink

# Create your views here.
def menu_view(request, category_title):
    if request.method == 'POST':
        category = Category.objects.get(category_title=category_title)
        drink = Drink.objects.filter(category=category)

    return render(request, 'menu.html', {'drink': drink})
