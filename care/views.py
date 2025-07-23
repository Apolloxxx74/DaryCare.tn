from django.contrib.auth import authenticate, login
from django.shortcuts import HttpResponse, HttpResponseRedirect, render,redirect
from django.urls import reverse
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'care/layout.html')
def quiz(request):
    return render(request, 'care/quiz.html')
def quiz0(request):
    return render(request, 'care/quiz0.html')


def register(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not email or not password:
            return render(request, "care/register.html", {"message": "Veuillez fournir un email et un mot de passe."})

        User = get_user_model()
        if User.objects.filter(username=email).exists():
            return render(request, "care/register.html", {"message": "Un compte avec cet email existe déjà."})

        user = User(username=email, email=email)
        user.password = make_password(password)
        user.save()

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")

        return redirect("login")
    else:
        return render(request, "care/register.html")







def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "care/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "care/login.html")
    

def services(request):

    return render(request, "care/services.html")

def espace_infirmier(request):

    if request.method == "POST":
            nom = request.POST.get("Nom_de_la_famille")
            prenom = request.POST.get("prenom")
            telephone = request.POST.get("telephone")
            date = request.POST.get("date")

            # Validation: check if all fields are filled
            if nom and prenom and telephone and date:
                return redirect('infirmier0')  # name from your urls.py
            else:
                return render(request, "care/espace_infirmier.html", {
                    "error": "Veuillez remplir tous les champs."
                })

        # GET request - show the form
    return render(request, "care/espace_infirmier.html")

def infirmier0(request):
    return render(request, "care/infirmier0.html")


def espace_patient(request):
    if request.method == "POST":
                nom = request.POST.get("Nom_de_la_famille")
                prenom = request.POST.get("prenom")
                telephone = request.POST.get("telephone")
                date = request.POST.get("date")

                # Validation: check if all fields are filled
                if nom and prenom and telephone and date:
                    return redirect('patient0')  # name from your urls.py
                else:
                    return render(request, "care/espace_patient.html", {
                        "error": "Veuillez remplir tous les champs."
                    })

            # GET request - show the form
    return render(request, "care/espace_patient.html")

def patient0(request):
    return render(request, "care/patient0.html")
