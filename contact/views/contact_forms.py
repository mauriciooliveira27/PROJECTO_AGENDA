from django.shortcuts import render, get_object_or_404,redirect
from django.views import View
from django.db.models import Q
from contact.models import Contact
from django.core.paginator import Paginator



class CreateView(View):
    template_name = 'contact/create.html'

    def get(self, request , *args , **kwargs):


        context = {

       

                }

        return render(request, self.template_name,context)