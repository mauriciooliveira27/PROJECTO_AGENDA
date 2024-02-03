from django.shortcuts import render, get_object_or_404,redirect
from django.views import View
from django.db.models import Q
from contact.models import Contact
from django.core.paginator import Paginator
from django import forms
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept':'image/*',
            }
        )
    )
    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'email', 'phone','description','cotegory','picture',
        )

@method_decorator(login_required(login_url='contact:login'), name='dispatch')
class CreateView(View):

    template_name = 'contact/create.html'
    form_action = reverse_lazy('contact:create')

    def get(self, request, *args, **kwargs):
        context = {
            'form': ContactForm(),
            'form_action': self.form_action,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST, request.FILES)
        context = {
            'form': form,
            'form_action': self.form_action,
        }
        if form.is_valid():
            contact = form.save()
            messages.success(request, 'Contact register with successfull')
            
            return redirect('contact:update', contact_id=contact.pk)
        return render(request, self.template_name, context)
    
@method_decorator(login_required(login_url='contact:login'), name='dispatch')
class UpdateView(View):

    template_name = 'contact/create.html'

    def get(self, request, contact_id):
        contact = get_object_or_404(Contact, pk=contact_id)
        form = ContactForm(instance=contact)
        form_action = reverse_lazy('contact:update', args=(contact_id,))
        context = {
            'form': form,
            'form_action': form_action,
        }
        return render(request, self.template_name, context)

    def post(self, request, contact_id):
        contact = get_object_or_404(Contact, pk=contact_id)
        form = ContactForm(request.POST, request.FILES, instance=contact)
        form_action = reverse_lazy('contact:update', args=(contact_id,))
        context = {
            'form': form,
            'form_action': form_action,
        }
        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.id)
        return render(request, self.template_name, context)


@method_decorator(login_required(login_url='contact:login'), name='dispatch')
class DeleteView(View):

    def post(self, request,contact_id):
        contact = get_object_or_404(Contact, pk=contact_id, show=True)
        print(contact)
        contact.delete()
        return redirect('contact:index')



class RegisterForm(UserCreationForm):
   
    class Meta:
        
        frist_name = forms.CharField(
        required=True
                )

        email = forms.EmailField(
        required=True
            )
        model = User
        fields = ( 'first_name','last_name', 'email','username', )

    def clean_email(self):

        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():

            self.add_error(
                'email',
                ValidationError('ja existe esse meial!')
            )

        return email
    
class RegistartUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ( 'first_name','last_name', 'email','username', )