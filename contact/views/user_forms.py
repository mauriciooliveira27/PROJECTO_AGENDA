from django.shortcuts import render, get_object_or_404,redirect
from django.views import View
from django.db.models import Q
from contact.models import Contact
from django.core.paginator import Paginator
from .contact_forms import RegisterForm, RegistartUpdateForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class RegisterView(View):   
    
    def get(self, request):
        
        form = RegisterForm()
        return render(
            request,'contact/register.html',{
                'form':form
            }
        )
    

    def post(self, request):
        
        form = RegisterForm()

        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'User register with successfull')
                return redirect('contact:index')
        return render(
            request,'contact/register.html',{
                'form':form
            }
        )
    

class LoginView(View):

     def get(self, request):
        
        form = AuthenticationForm()
        return render(
            request,'contact/login.html',{
                'form':form
            }
        )
     
     def post(self,request):
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)

        return redirect('contact:index')
    
@method_decorator(login_required(login_url='contact:login'), name='dispatch')
class LogoutView(View):
    def get(self,request):
        auth.logout(request)

        return redirect('contact:login')
    

@method_decorator(login_required(login_url='contact:login'), name='dispatch')
class UserUpdateView(View):
    def get(self, request):
        form = RegistartUpdateForm(instance=request.user)
        return render(
            request, 'contact/register.html',
            {
                'form':form
            }
        )
    
    def post(self, request):
        form = RegistartUpdateForm(data=request.POST, instance=request.user)
        if not form.is_valid():
    
            return render(
                request, 'contact/register.html',
                {
                    'form':form
                }
            )
        
        form.save()

        return render(
                request, 'contact/register.html',
                {
                    'form':form
                }
            )