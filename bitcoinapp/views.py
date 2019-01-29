from django.shortcuts import render
from django.views.generic import TemplateView
from django.db import connection
import requests

def replace(request):
        text = "replaced"
        return render(request, 'index.html', {'text': text}) 
        
def db_table_exists(table_name):
    return table_name in connection.introspection.table_names()        

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        text = "MARIO"
        return render(request, 'index.html', {'text': text})
   

class AboutPageView(TemplateView):
    template_name = "about.html"   

class step02PageView(TemplateView):
    template_name = "step2.html"     

class step03PageView(TemplateView):
    template_name = "step3.html"  