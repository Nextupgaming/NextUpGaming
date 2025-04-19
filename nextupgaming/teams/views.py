from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Team, TeamMembership
from .forms import TeamForm

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'teams/team_list.html', {'teams': teams})

@login_required
def team_create(request):
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            team = form.save()
            TeamMembership.objects.create(team=team, user=request.user, is_admin=True)
            return redirect('team_list')
    else:
        form = TeamForm()
    return render(request, 'teams/team_create.html', {'form': form})

def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    members = TeamMembership.objects.filter(team=team)
    return render(request, 'teams/team_detail.html', {'team': team, 'members': members})
