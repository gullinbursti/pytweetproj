# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
import twitter

def index(request):
    template = 'index.html'
    userName = request.POST.get( 'userTxt' )
    password = request.POST.get( 'passwordTxt' )

    if userName is not None and password is not None:        
        try:
            api = twitter.Api( username = userName, password = password) 
            # just grab the first 5 tweets
            statuses = api.GetUserTimeline()[0:5] 
            # limit to just the first 120
            following = api.GetFriends()[0:120] 
        except NameError, e:
            print "unable to login"

    else:
        statuses = {}
        following = False 

    # place values in session
    request.session['statuses'] = statuses
    request.session['following'] = following
    request.session['userName'] = userName
    request.session['password'] = password
    
    data = {
        'statuses' : statuses,
        'following' : following,
    }

    return render_to_response(template, data, 
           context_instance = RequestContext(request))


def panel(request):
    template = 'panel.html'
    data = {
        'statuses' : request.session['statuses'],
        'following' : request.session['following']
    }
    return render_to_response(template, data,
           context_instance = RequestContext(request))


def update(request):
    template = 'panel.html'
  
    userName = request.session['userName']
    password = request.session['password']
 
    try:
        api = twitter.Api( username = request.session['userName'], 
                           password = request.session['password']) 
        api.PostUpdate(request.POST.get('updateTextArea'))
        updated = True
        statuses = api.GetUserTimeline()[0:5] # reload the statuses
    except NameError, e:
        print "unable to login"
        updated = False

    data = {
        'userName' : request.session['userName'],
        'password' : request.session['password'],
        'updated'  : updated,
        'statuses' : statuses
    }
    return render_to_response(template, data,
           context_instance = RequestContext(request))