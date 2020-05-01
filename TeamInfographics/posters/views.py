from django.shortcuts import render
from posters.models import Lpz2019Teams, Lpz2019Locaties, Lpz2019Organisaties
from django.views import generic

import pandas as pd



# Create your views here.
def index(request):
    """View function for home page of site."""

    data = Lpz2019Teams.objects.get(id=1)

    context = {
        'data': data,
        'testname': 'Niels!'
    }

    # Render the HTML template index.html
    return render(request, 'poster.html', context=context)


class TeamDetailView(generic.DetailView):
    model = Lpz2019Teams

class LocatieDetailView(generic.DetailView):
    model = Lpz2019Locaties

class OrganisatieDetailView(generic.DetailView):
    model = Lpz2019Organisaties



