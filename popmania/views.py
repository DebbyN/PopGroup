# L2T23 - Capstone Project Django
# Sources - code snippets used from previous Assignment Tasks L2T18 to L2T23.

from django.shortcuts import get_object_or_404, render
#from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Question, Choice 

# Home page and login to site
def index(request):
    """
        This method will return the web home page for the popgroup
    """
    #template = loader.get_template('popmania/poppythons.html')
    #return HttpResponse(template.render())
    return render(request, 'popmania/poppythons.html')

# Login form
def login_user(request):
    """
        Method to return login page
    """
    return render(request, 'popmania/login.html')

# Page to register new users        
def register(request):
    """
     Method to return register page for new fans
    """
    return render(request, 'popmania/register.html')

# Process to register new users on the database    
def register_user(request):
    """Method to receive login username and password for verification in the database
    
        :raises error_message: User already on the system cannot create

        :returns: object method poll

        :rtype: python object method

    """
    username = request.POST['username']
    password = request.POST['password']
       
    if 'first_name' in request.POST:
        first_name = request.POST['first_name']
    else:
        first_name = ""
    last_name = ""
    email = ""
    
    #Check if user already in the database
    user = authenticate(username=username, password=password)
    if user is None:
        user = User.objects.create_user(
            username,first_name,password,)
        login(request,user)
        return HttpResponseRedirect(reverse('popmania:poll'))
    else:
        # Redisplay the home page
        #return HttpResponseRedirect(reverse('popmania:index'))
        # Redisplay the registering form 
        return render(request, 'popmania/register.html', {
            'error_message': "User already exists."
        })


# authenticate user login to database
def authenticate_user(request):
    """Method to authenticate the user in the database using the python authentication method from
        the django authentication library

        :raises: error_message: Invalid user message from database check

        :returns: object method poll

        :rtype: python object method
    """

    if 'username' in request.POST:
        username = request.POST['username']
    else:
        username = ""
    if 'password' in request.POST:
        password = request.POST['password']
    else:
        password = ""
            
    user = authenticate(username=username, password=password)
        
    if user is None:
        #Return to home page if user login details invalid.
        #return HttpResponseRedirect(reverse('popmania:index'))
        return render(request, 'popmania/login.html', {
            'error_message': "Invalid user credentials."
        })
        
    else:
        login(request,user)
        return HttpResponseRedirect(
            reverse('popmania:poll'))
    
# User logout process
def logout_user(request):
    """Method to logout user from database and display a farewell web page
        :returns: Farewell web page

        :rtype: html
    """
    logout(request)
    return render(request, 'popmania/logout.html')
    #return HttpResponse("Goodbye") 

# Poll page   
def poll(request):
    """Method to display the polls question list for voting

        :returns: Web page with context for option to select a question to vote on
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'popmania/poll.html', context)
    
# Details for voting on given questions
def detail(request, question_id):
    """Method to provide voting details on selected poll

        :param key question_id: The database id for the question record

        :returns: Question detail and voting web page

        :rtype: html
        :rtype: str
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'popmania/detail.html', {'question': question})

# Feedback on voting
def results(request, question_id):
    """Method provides feedback on all polls

        :param str Question: The question in the poll
        :param key question_id: The database id for the question record

        :returns: Results of all the polls

        :rtype: html
        :rtype: list 
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'popmania/results.html', {'question': question})
    #return HttpResponse(response)

# Vote on selected question
def vote(request, question_id):
    """Method is to collect votes for the selected poll
        
        :param: question_id key: Database key for the question record

        :raises: keyError: Error raised if no selection is made

        :returns: Input for the method called results
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(
            pk=request.POST['choice']
        )
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'popmania/detail.html', {
            'question': question,
            'error_message': "Please select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(
            reverse('popmania:results', args=(question_id,))
        )


