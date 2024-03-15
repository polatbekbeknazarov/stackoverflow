from django.shortcuts import render, redirect

from users.forms import ChangeProfileForm


def profile(request, username):
    if request.method == 'POST':
        form = ChangeProfileForm(instance=request.user, data=request.POST, files=request.FILES)

        if form.is_valid():
            form.save()

            return redirect('profile', request.user.username)
    else:
        form = ChangeProfileForm(instance=request.user)

    context = {
        'form': form,
    }
    
    return render(request, 'users/profile.html', context)
