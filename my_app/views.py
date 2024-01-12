from django.shortcuts import render, redirect,HttpResponse
from .models import User
from .form import cabri
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login,authenticate,logout
def register(request):
    if request.method == 'POST':     
        youssef = cabri(request.POST)
        if youssef.is_valid():
            # form.save(commit=False)
            # form.instance.email = form.cleaned_data['email']
            belier = youssef.save()
            print("tchai tchai yakoi le cabri",belier.username)
            return render(request, 'my_app/connexion.html')
    else :
        youssef = cabri()
    return render(request, 'my_app/register.html', {'youssef': youssef})
    
    
    # if request.method == 'POST':
    #     form = cabri(request.POST)
    #     if form.is_valid():
    #         # form.save(commit=False)
    #         # form.instance.email = form.cleaned_data['email']
    #         user = form.save()
    #         print(f"Utilisateur créé : nom: {user.username} password :{user.password} email: {user.email}")
    #         return render(request, 'my_app/connexion.html')
    # else:
    #     form = cabri()
    # return render(request, 'my_app/register.html', {'form': form})
       


def logine(request):
    if request.method == 'POST':
        password= request.POST["password"]
        username = request.POST["username"]
        context={"name":password}
        user= authenticate(request, password=password, username=username)
        print(user)
        print(f"password: {password}, email: {username}")
        if user is not None:
            login(request, user)
            return render(request, 'my_app/cabri.html')
        else:
            return HttpResponse("Échec de la connexion")
    return render(request, 'my_app/connexion.html')
        

# def logine(request):
#     if request.method == 'POST':
#         password= request.POST["password"]
#         email =request.POST["email"]
#         context={"name":password}
#         try:
#             user= User.objects.get(email=email)
#             if check_password(password,user.password):
#                 login(request, user)
#                 return HttpResponse("connecter")
#             else:
#                 return HttpResponse("echoué1")
#         except User.DoesNotExist:
#             return HttpResponse("echoué")
#     return render(request, 'my_app/connexin.html')
     


def logouts(request):
    logout(request)
    return redirect('logine')
    
def main(request):
    return render(request, 'my_app/cabri.html')