from django.shortcuts import render, get_object_or_404,redirect
from django.views import View
from django.db.models import Q
from contact.models import Contact
from django.core.paginator import Paginator
# Create your views here.


class IndexView(View):
    template_name = 'contact/index.html'

    def get(self, request , *args , **kwargs):
        contact    =   Contact.objects.filter(show=True).order_by('id')

        paginator = Paginator(contact, 25)
        page_number = request.GET.get("page")
        page_obj    =   paginator.get_page(page_number)

        context = {

                    'page_obj'      :   page_obj,
                    'site_title'    :   'Contatos - '

                }

        return render(request, self.template_name,context)
    
    


class ContactView(View):
    template_name = 'contact/index.html'

    def get(self, request, id):
        try:
            contacts = get_object_or_404(Contact, pk=id)
        except Contact.DoesNotExist:
            # Faça algo, como redirecionar para uma página de erro 404.
            pass
        

        contact_name    =   f'{contacts.first_name} {contacts.last_name} -'
        context         =   {
            'contact'       :   contacts,
            'site_title'    :   contact_name
        }

        return render(request, self.template_name, context)




class SearchView(View):

    template_name = 'contact/index.html'
    
    def get(self, request , *args , **kwargs):

        search_value    =   request.GET.get('q','').strip()
        if search_value ==  '':
            return redirect('contact:index')
        
        contacts    =   Contact.objects\
                        .filter(show=True)\
                        .filter(
                            Q(first_name__icontains     =   search_value)   |
                            Q(last_name__icontains      =   search_value)   |
                            Q(email__icontains          =   search_value)   |
                            Q(phone__icontains          =   search_value))\
                        .order_by('-id')
        paginator = Paginator(contacts, 25)
        page_number = request.GET.get("page")
        page_obj    =   paginator.get_page(page_number)

        context = {

                    'page_obj'      :   page_obj,
                    'site_title'    :   'Search - '

                }

        return render(request, self.template_name,context)