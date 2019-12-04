from django.shortcuts import render
from posters.models import Lpz2019V1 
import pandas as pd

df = pd.read_csv('I:/LPZ/Infographic/data/Data zorgaccent variabelen infographic_final.csv')


# Create your views here.
def index(request):
    """View function for home page of site."""

    data = Lpz2019V1.objects.all()

    context = {
        'data': data,
        'testname': 'Niels!'
    }

    # Render the HTML template index.html
    return render(request, 'poster.html', context=context)