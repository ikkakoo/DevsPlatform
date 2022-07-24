from multiprocessing import context
from django.shortcuts import render
from users.models import Profile

def profiles(request):
    profile = Profile.objects.all()
    context = {
        'profiles' : profile
    }
    return render(request, 'users/profiles.html', context)


def user_profile(request, pk):
    user_profile = Profile.objects.get(id=pk)

    top_skills = user_profile.skill_set.exclude(description__exact="")
    other_skills = user_profile.skill_set.filter(description="")

    context = {
        'profile' : user_profile,
        'top_skills' : top_skills,
        'other_skills' : other_skills,
    }
    return render(request, 'users/user_profile.html', context)
