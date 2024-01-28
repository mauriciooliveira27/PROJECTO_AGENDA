
from django.urls import path
from contact import views


app_name = 'contact'

urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    path('search/', views.SearchView.as_view(), name='search'),

    #contact (CRUD)
    path('contact/<int:id>/detail/', views.ContactView.as_view(), name='contact'),
    path('contact/create/', views.CreateView.as_view(), name='create'),
    # path('contact/<int:id>/update/', views.ContactView.as_view(), name='contact'),
    # path('contact/<int:id>/delete/', views.ContactView.as_view(), name='contact'),

]
