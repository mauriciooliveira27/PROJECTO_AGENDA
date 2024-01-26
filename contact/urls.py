
from django.urls import path
from contact import views




urlpatterns = [
    path('',views.IndexView.as_view(), name='index')
]
