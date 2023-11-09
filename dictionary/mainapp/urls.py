from django.conf import settings
from django.conf.urls.static import static

from . import views

from django.urls import path

urlpatterns = [
    path("", views.indexpage, name="index"),
    path("home", views.indexpage, name="index"),
    path("home/", views.indexpage, name="index"),
    path("words_list", views.wordspage, name="words"),
    path("words_list/", views.wordspage, name="words"),
    path("add_word", views.add_words, name="add_words"),
    path("add_word/", views.add_words, name="add_words"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
