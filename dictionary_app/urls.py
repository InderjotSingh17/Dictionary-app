from django.urls import path
from .views import get_word_meaning
urlpatterns = [
    path('', get_word_meaning, name='get_word_meaning'),
]