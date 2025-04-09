from django.urls import path

from . import views
urlpatterns = [
    path("", views.index,name="views"),
    path("<str:name>/", views.greet, name="greet")
]