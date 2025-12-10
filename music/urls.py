from django.urls import include, path
import music.views as view

urlpatterns = [
    path('',view.index, name='index'),
]