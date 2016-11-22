from django.shortcuts import render, HttpResponse

from . import forms


def index(request):
    return family_setup(request)


def family_setup(request):

    if request.method == 'POST':

        family_form = forms.FamilyForm(data=request.POST)
        if family_form.is_valid():
            family = family_form.save()
            return success(request, what='Family' + family.name)
        else:
            return HttpResponse('Invalid Family created')
    else:
        family_form = forms.FamilyForm()

    return render(request, 'System/index.html',
                  context={'given_form': family_form,
                           'action': 'Family'})


def rent_setup(request):

    if request.method == 'POST':

        rent_form = forms.RentForm(data=request.POST)
        if rent_form.is_valid():
            rent = rent_form.save()
            return success(request, what='Rent: '+rent.title)
    else:
        rent_form = forms.RentForm()

    return render(request, 'System/index.html',
                  context={'given_form': rent_form,
                           'action': 'Rent'
                           })


def success(request, what='Something'):
    return render(request, 'System/success.html', context={'act': what})

