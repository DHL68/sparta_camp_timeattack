from django.urls import path
from . import views

urlpatterns = [
    path('sign-up-sparta/', views.sign_up_view, name='sign-up'),
]