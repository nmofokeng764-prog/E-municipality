from django.shortcuts import render
from django.http import HttpResponse




def home(request):
    return render(request, 'main/home.html')
  
def report(request):
    return render(request, 'main/report.html')

def viewreport(request):
    return render(request, 'main/viewreport.html')

def contact(request):
    return render(request, 'main/contact.html')

def report_issue(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('email_or_phone')
        issue_type = request.POST.get('issue_type')
        location = request.POST.get('location')
        description = request.POST.get('description')
        severity = request.POST.get('severity')

        print(name, contact, issue_type, location, description, severity)

    return render(request, 'main/report.html')

