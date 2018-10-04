from django.shortcuts import render
from django.utils import timezone
from .models import Character, active_Character

# Tries to get the current IP_Adress.
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


# Checks if a character is marked as active. If not, choose or create one. Last part isn't implemented yet.
def start(request):
    if request.user.is_authenticated:
        username = request.user
        characters = Character.objects.filter(user=username)
        active = active_Character.objects.get(user=username)
        if active.char is not None:
            active.char.last_login = timezone.now()
            ip = get_client_ip(request)
            try:
                test = Character.objects.get(ip_adress__contains=ip, id=active.char.id)
            except Character.DoesNotExist:
                test = None
            if test is not None:
                if test.id == active.char.id:
                    ip = ip
            else:
                active.char.ip_adress = active.char.ip_adress + ', ' + ip
                active.char.save(update_fields=['last_login', 'ip_adress'])
            
        return render(request, 'usermanagement/start.html', {'characters': characters, 'username': username, 'active': active, 'test': test})  
    else:
        username = "not logged in"
    return render(request, 'usermanagement/start.html', {'username': username})