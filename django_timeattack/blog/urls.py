from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.Article, name='tweet')
]