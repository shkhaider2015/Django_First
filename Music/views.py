from django.http import HttpResponse
from django.template import loader
from .models import Album
def index(request):
    all_albums = Album.objects.all()
    template = loader.get_template("")
    # html = ""
    # for album in all_albums:
    #     url = "/music/" + str(album.id) + "/"
    #     html += "<a href=" + url + ">" + album.album_tittle + "</a><br>"
    return HttpResponse()
def detail(request, album_id):
    return HttpResponse("<h2>Details For Album id:"+ str(album_id)+" </h2>")
