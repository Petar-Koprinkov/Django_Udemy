from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


month_fictionary = {
    'january': 'Learn Python.',
    'february': 'Learn JavaScript.',
    'march': 'Learn Java.',
    'april': 'Learn C++.',
    'may': 'Learn Django.',
    'june': 'Learn C#.',
    'july': 'Learn Docker.',
    'august': 'Learn HTML.',
    'september': 'Learn CSS.',
    'october': 'Learn Django ORM.',
    'november': None,
    'december': 'Learn GIT  .',
}


def index(request):
    months = list(month_fictionary.keys())
    context = {
        'months': months,
    }
    return render(request, 'challenges/index.html', context)


def number_month_challenge(request, month):
    try:
        months = list(month_fictionary.keys())
        chosen_month = months[month - 1]
        return HttpResponseRedirect(reverse('mouth_challenge', args=[chosen_month]))
    except:
        return HttpResponseNotFound('<h2>INVALID MONTH!</h2>')


def month_challenge(request, month):
    try:
        text = month_fictionary[month]
        context = {
            'month': month,
            'text': text
        }
        return render(request, 'challenges/challenge.html', context)
    except:
        return HttpResponseNotFound('<h2>INVALID PAGE!</h2>')
