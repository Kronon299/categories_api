from django.urls import path
from .views import CategoryView
app_name = "categories"


urlpatterns = [
    path('', CategoryView.as_view()),
]