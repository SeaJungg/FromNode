from django.shortcuts import render, redirect

'''
#Session Create
def login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
        return redirect('index')
    
    else:
        login_form = AuthenticationForm()
    
    return render(request, 'account/login.html', {'login_form' : login_form})

def signup(request):
    if request.method == 'POST':
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
        return redirect('index')
    else:
        signup_form = UserCreationForm()
    return render(request, 'account/signup.html', {'signup_form':signup_form})


def logout(request):
    auth_logout(request)
    return redirect('posts:list')
'''