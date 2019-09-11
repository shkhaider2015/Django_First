from django.conf.urls import url
from django.urls import include, path
from . import views

app_name = "music"

urlpatterns = [
# /Music/
    path('', views.index, name='index'),
# /Music/729/
    # url(r"^(?P<album_id>[0-9] + )$", view.detail, name="detail")
    path("<int:album_id>/", views.detail, name="detail"),

    #/Music/id/favorite
    path("<int:album_id>/favorite", views.favorite, name="favorite")
]