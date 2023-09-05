from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #name= 'Patrick'
    #from a database, it will be something like
    # name = user.name
    # if we have multiple data, we can use context
    context = {
        'name': 'Patrick',
        'age': 25,
        'nationality':'Nigerian'
    }

    return render(request,'index.html', context)
