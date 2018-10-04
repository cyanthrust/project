from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.utils import timezone
from usermanagement.models import Character, active_Character
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def all_user(request):
    username = request.user
    active = active_Character.objects.get(user=username)
    characters = Character.objects.order_by('created_date')
    return render(request, 'dashboard/all_user.html', {'characters': characters, 'username': username, 'active': active})

def profile(request, firstname, lastname):
    try:
        character = Character.objects.get(firstname__iexact=firstname, lastname__iexact=lastname)
    except Character.DoesNotExist:
        raise Http404("Nothing here does not exist")
    return render(request, 'dashboard/profile.html', {'character': character})

