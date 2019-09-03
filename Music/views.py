from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1>This is Music App Home Page</h1>")
def detail(request, album_id):
    return HttpResponse("<h2>Details For Album id:"+ str(album_id)+" </h2>")
