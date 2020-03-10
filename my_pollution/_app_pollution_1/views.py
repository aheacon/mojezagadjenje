from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render

from .models import *
from .scrapp_data import *

# Create your views here.
# Route: /dummy_so2
def dummy(request):
    #return HttpResponse("Hi dummy!")
    template_name="_ns_pollution_1/dummy.html"
    context={
      'table_so2': table_so2.objects.all()
    } #context dictionary passes keys and values
    return render(request, template_name, context)
# Route: /
def index(request):
    # Dobivanje gradova i prognoze vremena
    gradovi= get_cities()
    url= gradovi["Zenica"][0]["url"]
    #return HttpResponse(gradovi["Zenica"][0]["url"])
    aqi= scrap_aqi()
    template_name="_ns_pollution_1/index.html"
    context={
      'url_grad': url,
      'aqi':aqi
    } 
    return render(request, template_name, context)
