from django.shortcuts import render

# Create your views here.
def workouts(request):
    return render(request,'workouts.html')


def totalwork(request):
    return render(request,'totalwork.html')

def absss(request):
    return render(request,'absss.html')

def arms(request):
    return render(request,'arms.html')

def legs(request):
    return render(request,'legs.html')