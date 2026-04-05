from django.shortcuts import render

def feedback_home(request):
    #return render(request, 'home.html')
    return render(request, 'feedback/feedback.html')

# Create your views here.
