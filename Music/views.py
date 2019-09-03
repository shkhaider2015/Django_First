from django.http import HttpResponse
from .models import Album
def index(request):
    all_albums = Album.objects.all()
    html = ""
    for album in all_albums:
        url = "/music/" + str(album.id) + "/"
        html += "<a href=" + url + ">" + album.album_tittle + "</a><br>"

    return HttpResponse(html)
def detail(request, album_id):
    return HttpResponse("<h2>Details For Album id:"+ str(album_id)+" </h2>")
