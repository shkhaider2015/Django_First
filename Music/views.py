from django.http import HttpResponse
from django.shortcuts import render
from .models import Album
def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    # html = ""
    # for album in all_albums:
    #     url = "/music/" + str(album.id) + "/"
    #     html += "<a href=" + url + ">" + album.album_tittle + "</a><br>"
    return render(request, "music/index.html", context)
def detail(request, album_id):
    return HttpResponse("<h2>Details For Album id:"+str(album_id)+" </h2>")
