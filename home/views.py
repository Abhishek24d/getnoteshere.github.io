from django.shortcuts import render, HttpResponse
from home.models import Contact
from datetime import datetime
# import docx
# Create your views here.


def index(request):
    return render(request, 'index.html',)


def field(request):
    return render(request, 'field.html')


def content(request):
    return render(request, 'e.next.html')


def fe_bee(request):
    return render(request, 'bee.html')


def bee_unit1(request):
    return render(request, 'bee_unit1.html')


def bee_unit2(request):
    return render(request, 'bee_unit2.html')


def bee_unit3(request):
    return render(request, 'bee_unit3.html')


def bee_unit4(request):
    return render(request, 'bee_unit4.html')


def bee_unit5(request):
    return render(request, 'bee_unit5.html')


def bee_unit6(request):
    return render(request, 'bee_unit6.html')


def fe_ec(request):
    return render(request, 'ec.html')


def ec_unit1(request):
    return render(request, 'ec_unit1.html')


def ec_unit3(request):
    return render(request, 'ec_unit3.html')


def ec_unit4(request):
    return render(request, 'ec_unit4.html')


def ec_unit5(request):
    return render(request, 'ec_unit5.html')


def ec_unit6(request):
    return render(request, 'ec_unit6.html')


def about(request):
    return render(request, 'about.html')


def service(request):
    return render(request, 'service.html')


def contact(request):
    if request.method == 'POST':
        email = request.POST.get('Email')
        pass1 = request.POST.get('Password')
        date = datetime.today()
        contact = Contact(email = email, pass1 = pass1, date = date)
        contact.save()
    return render(request, 'contact.html')


def technical(request):
    return render(request, 'technical.html')


