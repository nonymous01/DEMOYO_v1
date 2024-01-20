from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from django.shortcuts import render,HttpResponse
from django.shortcuts import get_object_or_404

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


# def update(request, id):
#     x = Article.objects.get(id=id)
#     x.description = "description"
#     x.titre = "titre"

#     x.save()
#     return render(request,"update.html",context= {"context":x})


def update(request, id):
    
    x = Article.objects.get(id=id)
    
    context={} 
    form = ArticleForm(request.POST or None)
    x.description  = str(form["description"].value())  
    x.titre = str(form["titre"].value()) 
    x.save()
    # print(form["titre"].value())
    # print(form["description"].value())
    context['form']=form
    return render(request,"update.html", context)

def delete(request, id):
    context={}
    context["datas"]=Article.objects.all()
    x = Article.objects.get(id=id)
    x.delete()
    return render(request,"list.html", context)