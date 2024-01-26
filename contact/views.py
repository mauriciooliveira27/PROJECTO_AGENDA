from django.shortcuts import render
from django.views import View

# Create your views here.


class IndexView(View):

    template_name = 'contact/index.html'

    def get(self, request , *args , **kwargs):
        return render(request, self.template_name)