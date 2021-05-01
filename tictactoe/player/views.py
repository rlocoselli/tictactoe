from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from gameplay.models import Game
from .forms import InvitationForm
from .models import Invitation
# Create your views here.

@login_required
def home(request):
    games_first_player = Game.objects.filter(
        first_player=request.user,
        status = "F"
    )
    games_second_player = Game.objects.filter(
        second_player=request.user,
        status = "S"
    )

    invitations = request.user.invitations_received.all()

    all_my_games = list(games_first_player) + list(games_second_player)

    return render(request, "player/home.html", {"games": all_my_games, "invitations": invitations})

@login_required
def new_invitation (request):

    form = decideActionAndExecute(request)

    if(request.method != "POST"):
        return render(request, "player/new_invitation_form.html", {"form": form})
    else:
        return redirect("player_home")

@login_required
def accept_invitation(request, id):
    
    invitation = get_object_or_404(Invitation, pk=id) 
    if not request.user == invitation.to_user:
        raise PermissionDenied
    if request.method == "POST":
        if "accept" in request.POST:
            game = Game.objects.create(
                first_player=invitation.to_user,
                second_player=invitation.from_user,
            )

        invitation.delete()
        return redirect("game")
    else:
        return render(request,"player/accept_invitation_form.html",
                      {"invitation": invitation})

def decideActionAndExecute(request):
    if request.method == "POST":
        invitation = Invitation(from_user=request.user)
        form = InvitationForm(instance=invitation, data=request.POST)
        if(form.is_valid()):
            form.save()
    else:
        form = InvitationForm()
    
    return form

