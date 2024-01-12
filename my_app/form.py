from django import forms
from django.contrib.auth.forms import UserCreationForm


class cabri(UserCreationForm):
    # username = forms.CharField(
    #     label="enter your username",
    #     strip=False,
    #     widget=forms.PasswordInput(attrs={"autocomplete": "username"})
    # )
    email = forms.CharField(
        label="enter your email",
        # strip=False,
        widget=forms.TextInput(attrs={"autocomplete": "email"}),
    )
    password1 = forms.CharField(
        label="enter your password1",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    password2 = forms.CharField(
        label="enter your password2",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    class Meta(UserCreationForm.Meta):
        fields= UserCreationForm.Meta.fields + ("password1","password2")


    def __init__(self, *args, **kwargs) :
        super(cabri,self).__init__(*args, **kwargs)
        self.fields["username" ].widget.attrs["placeholder"]= 'enter your name'
        self.fields["email" ].widget.attrs["placeholder"]= 'enter your email'
        self.fields["password1" ].widget.attrs["placeholder"]= 'enter your password1'
        self.fields["password2" ].widget.attrs["placeholder"]= 'enter your password2 confirm'
        


# from  django import forms
# from django.contrib.auth.forms import UserCreationForm


# class cabri(UserCreationForm):
#     email = forms.EmailField(
#         label="entrer un e-mail",
#         required=True,
#         widget=forms.TextInput(attrs={'autocomplete': 'email'}),
#         #help_text="Required. 150 characters or fewer. Lettersand @/./+/-/_ only.",
#     )
#     password1 = forms.CharField(
#         label="entrer un mot de passe",
#         widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}), 
#     )

#     password2 = forms.CharField(
#         label="confirmation de mot de passe",
#         widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}), 
#     )
# #class meta pour personnaliser les chants du formulaire
#     class Meta(UserCreationForm.Meta):
#         fields=UserCreationForm.Meta.fields +("password1","password2")


#     def __init__(self, *args, **kwargs):
#         super(cabri, self).__init__(*args, **kwargs)
#         # Ajoutez le placeholder pour chaque champ ici
#         self.fields['username'].widget.attrs['placeholder'] = 'Nom d\'utilisateur'
#         self.fields['password1'].widget.attrs['placeholder'] = 'Mot de passe'
#         self.fields['password2'].widget.attrs['placeholder'] = 'Confirmer le mot de passe'
#         self.fields['email'].widget.attrs['placeholder'] = 'Adresse e-mail'







# from typing import Any
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# # runserver
# class CabriUserCreationForm(UserCreationForm):
#     username = forms.CharField(
#         label="Enter your username",
       
#         widget=forms.TextInput(attrs={"autocomplete": "username"}),
#     )
#     email = forms.CharField(
#         label="Enter your email",
       
#         widget=forms.TextInput(attrs={"autocomplete": "email"}),
#     )
#     password1 = forms.CharField(
#         label="Enter your password",
       
#         widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
#     )
#     password2 = forms.CharField(
#         label="Confirm your password",
       
#         widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
#     )

#     class Meta(UserCreationForm.Meta):
#         fields = UserCreationForm.Meta.fields + ("password1", "password2")

#     def __init__(self, *args: Any, **kwargs: Any):
#         super(CabriUserCreationForm, self).__init__(*args, **kwargs)
#         self.fields["username"].widget.attrs["placeholder"] = 'Enter your name'
#         self.fields["email"].widget.attrs["placeholder"] = 'Enter your email'
#         self.fields["password1"].widget.attrs["placeholder"] = 'Enter your password'
#         self.fields["password2"].widget.attrs["placeholder"] = 'Confirm your password'
