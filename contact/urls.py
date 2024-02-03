
from django.urls import path
from contact import views


app_name = 'contact'

urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    path('search/', views.SearchView.as_view(), name='search'),

    #contact (CRUD)
    path('contact/<int:id>/detail/', views.ContactView.as_view(), name='contact'),
    path('contact/create/', views.CreateView.as_view(), name='create'),
    path('contact/<int:contact_id>/update/', views.UpdateView.as_view(), name='update'),
    path('contact/<int:contact_id>/delete/', views.DeleteView.as_view(), name='delete'),

    
    path('user/register/', views.RegisterView.as_view(), name='register'),
    path('user/login/', views.LoginView.as_view(), name='login'),
    path('user/logout/', views.LogoutView.as_view(), name='logout'),
    path('user/update/', views.UserUpdateView.as_view(), name='user_update')

]
