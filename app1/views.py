from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    #name= 'Patrick'
    #from a database, it will be something like
    # name = user.name
    # if we have multiple data, we can use context
    #context = {
    #    'name': 'Patrick',
    #    'age': 25,
    #    'nationality':'Nigerian'
    #}
    
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'fast'
    feature1.details = ' Our service is fast'

    return render(request,'index.html') #add context inside the parentheses to render the data


def counter(request):
    text = request.POST['text']
    amount_of_words= len(text.split())
    return render(request,'counter.html' , {'amount': amount_of_words})
