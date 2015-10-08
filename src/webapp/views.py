from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from webapp.models.bean import Region, Bean
from django.shortcuts import redirect

def site_login(request):
    login_feedback = None
    next_url = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.POST.get('next_url')
        if not next_url:
            next_url = "index"
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                return redirect(next_url)
            else:
                # Return a 'disabled account' error message
                login_feedback = "This account is disabled."
        else:
            # Return an 'invalid login' error message.
            login_feedback = "Invalid username and/or password."
    # plain GET or unsuccessful POST, show login page
    return render(request, 'webapp/login.html', {
            'title': 'Login to FizzBuzz',
            'user': request.user,
            'hide_login': True, # hides the login link on the main template
            'login_feedback' : login_feedback,
            'next_url': next_url,
        })


def site_logout(request):
    logout(request)
    return redirect("index")
