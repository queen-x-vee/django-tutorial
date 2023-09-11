from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth 
from django.contrib import messages
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
    '''
    feature1.id = 0
    feature1.name = 'fast'
    feature1 = Feature()
    feature1.details = ' Our service is fast'
    feature1.is_true = True

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'reliable'
    feature2.details = ' Our service is reliable'
    feature2.is_true = True

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'easy to use'
    feature3.details = ' Our service is easy to use'
    feature3.is_true = False

    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'affordable'
    feature4.details = ' Our service is affordable'
    feature4.is_true = True

    features = [feature1, feature2, feature3, feature4]
    '''
    features = Feature.objects.all()
    return render(request,'index.html', {'features' : features,}) #add context inside the parentheses to render the data

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request, 'Email already in use')
                return redirect('register')
            
            elif User.objects.filter(username = username).exists():
                messages.info(request, 'Username already in use')
 
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
            
        else:
            messages.info(request, 'Password not the same')
            return redirect('register')
        
    else:
        return render(request, 'register.html')


    return render(request, 'register.html')

def login (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        
        else:
            messages.info(request, 'Credentials Invalid')

    else:
        return render (request, 'login.html')

def logout (request):
    auth.logout(request)
    return redirect('/')

'''
def counter(request):
    text = request.POST['text']
    amount_of_words= len(text.split())
    return render(request,'counter.html' , {'amount': amount_of_words})
'''

def counter(request):
    posts = [1,2,3,4,5,'tim', 'tina', 'tony']
    #posts can be an object from the database. as in blog posts from a url
    return render(request,'counter.html' , {'posts': posts})

def post (request, pk):
    return render(request, 'post.html',{'pk':pk})