from django.shortcuts import render
from .models import Profile
from .forms import ProfileModelForm
from django.contrib import messages


def my_profile_view(request):
    profile = Profile.objects.get(user=request.user)
    profile_form = ProfileModelForm(request.POST or None, request.FILES or None, instance=profile)
    confirm = False

    if request.POST:
        if profile_form.is_valid():
            profile_form.save()
            confirm = True

    context = {
        'profile': profile,
        'form': profile_form,
        'confirm': confirm
    }
    return render(request, 'profiles/myprofiles.html', context)
