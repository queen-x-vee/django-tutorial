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

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'reliable'
    feature2.details = ' Our service is reliable'

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'easy to use'
    feature3.details = ' Our service is easy to use'

    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'affordable'
    feature4.details = ' Our service is affordable'

    feature5 = Feature()
    feature5.id = 4
    feature5.name = 'trustworthy'
    feature5.details = ' Our service is trustworthy'

    features = [feature1, feature2, feature3, feature4, feature5]

    return render(request,'index.html', {'features' : features,}) #add context inside the parentheses to render the data


def counter(request):
    text = request.POST['text']
    amount_of_words= len(text.split())
    return render(request,'counter.html' , {'amount': amount_of_words})
