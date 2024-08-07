from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

month_fictionary = {
    'january': 'This is the first day of January.',
    'february': 'This is the first day of February.',
    'march': 'This is the first day of March.',
    'april': 'This is the first day of April.',
    'may': 'This is the first day of May.',
    'june': 'This is the first day of June.',
    'july': 'This is the first day of July.',
    'august': 'This is the first day of August.',
    'september': 'This is the first day of September.',
    'october': 'This is the first day of October.',
    'november': 'This is the first day of November.',
    'december': 'This is the first day of December.',
}


def index(request):
    months = list(month_fictionary.keys())
    months_list = [f'<li><a href="{reverse('mouth_challenge', args=[m])}">{m}</a></li>' for m in months]
    return HttpResponse(months_list)


def number_month_challenge(request, month):
    try:
        months = list(month_fictionary.keys())
        chosen_month = months[month - 1]
        return HttpResponseRedirect(reverse('mouth_challenge', args=[chosen_month]))
    except:
        return HttpResponseNotFound('INVALID MONTH!')


def month_challenge(request, month):
    try:
        return HttpResponse(month_fictionary[month])
    except:
        return HttpResponseNotFound('INVALID MONTH!')
