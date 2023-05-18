from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def demo(request):
    return render(request, 'base.html')


def newpage(request):
    return render(request, 'main.html')


from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('loginpage')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        confirm_password = request.POST['password1']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name)

                user.save();
                return redirect('login')
        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('/')

    return render(request, "register.html")


def loginpage(request):
    return render(request, 'main.html')


def forms(request):
    return render(request, 'forms.html')


def registration(request):
    return


def logout(request):
    auth.logout(request)
    return redirect('/')


def lastpage(request):
    return render(request, 'last.html')

from django.http import JsonResponse

def get_cities(request):
    CITIES_BY_DISTRICT = {
        'Thrissur': ['Chalakudy', 'Kodungallur', 'Koratty', 'Triprayar', 'Thrissur'],
        'Ernakulam': ['Aluva', 'Nettoor', 'Edapally', 'Vypin', 'Poothotta'],
        'Palakad': ['Shornur', 'Pattambi', 'Cherupulassery', 'Malampuzha', 'Chittur'],
    }
    district = request.GET.get('district')
    cities = CITIES_BY_DISTRICT.get(district, [])
    return JsonResponse({'cities': cities})
