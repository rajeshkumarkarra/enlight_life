from django.shortcuts import render
#from django.template import Context
from .models import Fundraise


# Create your views here.
def index(request):
    """
    #object of class in models.py
    fund = Fundraise()
    #initialize the class content  
    fund.dis = 'Food to Poor'
    fund.img = 'passion_1.png'
    fund.goal = 10050.10
    fund.raised = 9050.01
    # if skill count True then only shows the skill bar in index.html
    fund.skillcount = True

    #object of class in models.py
    fund1 = Fundraise()
    #initialize the class content  
    fund1.dis = 'Reduce an Unemployment'
    fund1.img = 'passion_2.png'
    fund1.goal = 14505.10
    fund1.raised = 2324.01
    # if skill count True then only shows the skill bar in index.html
    fund1.skillcount = False

    #object of class in models.py
    fund2 = Fundraise()
    #initialize the class content  
    fund2.dis = 'Adopt a Child'
    fund2.img = 'passion_3.png'
    fund2.goal = 18088.10
    fund2.raised = 15050.01
    # if skill count True then only shows the skill bar in index.html
    fund2.skillcount = True

    funds =[fund, fund1, fund2]
    """
    funds = Fundraise.objects.all()
    return render(request, 'ngo/index.html', {'funds':funds})

