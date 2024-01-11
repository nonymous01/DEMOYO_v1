from django.shortcuts import render, redirect,HttpResponse
from .models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login,authenticate
def register(request):
    if request.method == 'POST':     
        username = request.POST.get('username')
        email = request.POST.get("email")
        password= request.POST.get('password')
        user = User.objects.create(name=username, email=email, password=password)
        user.save()
        return render(request, 'my_app/connexion.html')
    return render(request, 'my_app/register.html')


def logine(request):
    if request.method == 'POST':
        password= request.POST["password"]
        email =request.POST["email"]
        context={"name":password}
        user= authenticate(request, password=password, email=email)
        print(f"nom: {password}, email: {email}")
        if user is not None:
            login(request, user)
            return redirect("main")
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
     

def main(request):
    return render(request, 'my_app/cabri.html')