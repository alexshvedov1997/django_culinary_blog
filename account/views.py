from django.shortcuts import render
from .forms import UserRegestrationForm

def register(request):
    if request.method == 'POST':
        user_form = UserRegestrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request,"account/success_create.html", { 'new_user':new_user})
    else:
        user_form = UserRegestrationForm()
    return render(request, "account/register_form.html", {'user_form':user_form})


# Create your views here.
