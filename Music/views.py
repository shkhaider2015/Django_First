from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1>This is Music App Home Page</h1>")
