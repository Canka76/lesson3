import datetime
from django.shortcuts import render

# Create your views here.

def index(request):
    # Get the current date and time
    now = datetime.datetime.now()
    
    # Check if today is New Year's Day (January 1st)
    return render(request, "newyear/index.html", {
        "newyear": now.month == 1 and now.day == 1
    })
