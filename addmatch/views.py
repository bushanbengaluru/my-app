from django.shortcuts import render

# Create your views here.
def add_match(request):
    return render(request, 'addmatch/add_match.html')