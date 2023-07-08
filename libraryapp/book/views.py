
from django.shortcuts import render

# Create your views here.
 
# relative import of forms
from .models import GeeksModel
from .forms import GeeksForm
 
 
def create_view(request):
    # dictionary for initial data with field names as keys
    context ={}
    # add the dictionary during initialization
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form']= form
    return render(request, "create_view.html", context)

def list_view(request):
    context = {}
    #add the dictionary during the initialisation
    context["dataset"]=GeeksModel.objects.all()
    return render(request, "list_view.html", context)

