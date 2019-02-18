from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def loginSuccess(request):
    print(request.POST)
    n = request.POST.get("firstname")
    return render(request, 'home/loginSuccess.html', {'firstname': n})
