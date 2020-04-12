from django.shortcuts import render

# Create your views here.
def dream_list(request):
    return render(request, 'myapp/dream_list.html', {})