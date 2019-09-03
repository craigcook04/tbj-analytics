from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import JsonResponse
from django.shortcuts import render

import csv, json, urllib

from .models import Player, Team
from .forms import searchForm

IMPORT_URL = "https://statsapi.mlb.com/api/v1/teams/141/roster/Active?%20hydrate=person(stats(type=season))"

# Create your views here.

# Home Page
def index(request):
    playersList = Player.objects.order_by('lastName')[:5]
    template = loader.get_template('jays_app/index.html')
    context = {
        # playersList refers to the 'Player' model in SQLite
        'playersList': playersList, 
    }
    return HttpResponse(template.render(context, request))

# Get MLB teams JSON
def teams(request):
    teamsList = Team.objects.order_by('teamId')
    # MLB Teams
    # if(MLBfilter):
    url = ("https://statsapi.mlb.com/api/v1/teams?sportId=1")
    # ALL Teams
    # url = ("https://statsapi.mlb.com/api/v1/teams")
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
    template = loader.get_template('jays_app/teams.html')
    context = {
        'teams': data,
        'teamsList': teamsList,
        # 'MLBfilter': MLBfilter
    }
    return HttpResponse(template.render(context, request))

# Get roster for selected team
def roster(request, teamId):
    url = ("https://statsapi.mlb.com/api/v1/teams/" + teamId + "/roster")
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
    with urllib.request.urlopen("https://statsapi.mlb.com/api/v1/teams/" + teamId) as url:
        teamData = json.loads(url.read().decode())
    template = loader.get_template('jays_app/roster.html')
    context = {
        'roster': data,
        'teamData': teamData
    }
    return HttpResponse(template.render(context, request))

# Get MLB players JSON for specific team
def players(request, playerId):
    url = ("https://statsapi.mlb.com/api/v1/people/" + playerId + "?hydrate=stats(group=[hitting,pitching,fielding],type=[yearByYear])")
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
    template = loader.get_template('jays_app/players.html')
    context = {
        'players': data,
    }
    return HttpResponse(template.render(context, request))

def search(request):
    # url = ("https://statsapi.mlb.com/api/v1/teams/" + teamId + "/roster")
    # with urllib.request.urlopen(url) as url:
    #     data = json.loads(url.read().decode())
    template = loader.get_template('jays_app/search.html')
    context = {
    #     'roster': data,
    }
    return HttpResponse(template.render(context, request))

# About Me
def about(request):
    template = loader.get_template('jays_app/about.html')
    context = {}
    return HttpResponse(template.render(context, request))

# Download File
def generateReport(request, playerId):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="playerReport.csv"'
    writer = csv.writer(response)
    url = ("https://statsapi.mlb.com/api/v1/people/" + playerId + "?hydrate=stats(group=[hitting,pitching,fielding],type=[yearByYear])")
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
    template = loader.get_template('jays_app/players.html')
    context = {
        'players': data,
    }
    if data:
        writer.writerow(['Player ID', playerId])
        writer.writerow(['JSON', data])
    return response