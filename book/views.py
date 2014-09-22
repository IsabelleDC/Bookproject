from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from book.forms import LivreForm, GenreForm, EmailUserCreationForm
from book.models import Livre, Visitor, Genre


def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')

def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password1"]
            user = form.save()
            user.email_user("Welcome!", "Thank you for signing up for our website.")
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("profile")
    else:
        form = EmailUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })

@login_required()
def new_livre(request):
    if request.method =='POST':
        form = LivreForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/genres")
    else:
        form = LivreForm()

    data = {'form': form}
    return render(request, 'new_livre.html', data)
#
@login_required()
def livres(request, category_id):
    livres = Livre.objects.filter(genres__id=genre_id)
    return render(request, 'livres.html', {'livres': livres})

@login_required()
def new_genre(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            name = request.POST["name"]
            Genre.objects.create(user=request.user, name =name)
            return redirect("/livres")
    else:
        form = GenreForm()

    data = {'form': form}
    return render(request, 'new_genre.html', data)

@login_required()
def genres(request):
    genres= Genre.objects.filter(user=request.user)
    return render(request, 'genres.html', {'genres': genres})

def map(request, location_id):
    location = Livre.objects.filter(id=location_id)
    for place in location:
        country = place.country
        city = place.city
        street = place.street
        streetnum = place.streetnum
        address ='{}, {}, {}, {}'.format(country, city, street, streetnum)

    return render (request, 'map.html', {'address': address})
