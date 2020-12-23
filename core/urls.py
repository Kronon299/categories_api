from django.urls import path
from .views import CategoriesView, CategoryDetailView
app_name = "categories"


urlpatterns = [
    path('', CategoriesView.as_view()),
    path('<int:pk>/', CategoryDetailView.as_view()),
]