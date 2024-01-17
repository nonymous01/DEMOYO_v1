from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse


from .forms import ArticleForm
from .models import Article


def create_view(request):
    context={} #Crée un dico vide 
    form = ArticleForm(request.POST or None)#Vérifier la method avec la class du form.py
    if form.is_valid():# Véerifier si le formullaire a éte bien rempli
        form.save()# enregistré si c'est valide
    context['form']=form # recuperer form dans contex
    return render(request,"index.html", context)



def list_view(request):
    context={}
    context["datas"]=Article.objects.all()
    return render(request,"list.html", context)


def detail_view(request, id):
    context={}
    context["data"]=Article.objects.get(id=id)
    return render(request, "detail_view.html", context)