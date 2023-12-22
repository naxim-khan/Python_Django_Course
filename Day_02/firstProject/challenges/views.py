from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthlyCh={
    "january":"january Month",
    "february":"february Month",
    "march":"march Month",
    "april":"april Month",
    "june":"june Month",
    "july":"july Month",
    "august":"august Month",
    "september":"september Month",
    "october":"october Month",
    "november":"november Month",
    "december":"december Month",
}


def index(request):
    list_items = ""
    months = list(monthlyCh.keys())

    for month in months:
        capitalized_month= month.capitalize()
        month_path = reverse("month-challenge",args=[month])
        list_items += f"<li> <a href=\"{month_path}\">{capitalized_month} </a> </li>"
    response_data = f"<h1><ul>{list_items}</ul></h1>"
    return(HttpResponse(response_data))



def numbers(request, month):
    # response_text = f"You are viewing month: {month}"  # Or any desired content
    months=list(monthlyCh.keys() ) # return value at expected index
    if month>len(months):
        return HttpResponseNotFound("invalid month")
    forward_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[forward_month])

    return HttpResponseRedirect(redirect_path)

def monthlyChallenges(request, month):
    month=month.lower()
    try:
        challenge_text = monthlyCh[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("this month is not supported!!!")

    

    
