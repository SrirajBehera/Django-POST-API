from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

def index(request):
    return render(request, 'index.html')

@csrf_protect
def calculate(request):
    value = int(request.POST['numbox'])
    fact = 1
    for i in range(1, value + 1):
        fact = fact * i
    params = {'number': value, 'result': fact}
    return render(request, 'result.html', params)