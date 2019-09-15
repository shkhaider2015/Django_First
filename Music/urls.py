from django.conf.urls import url
from django.urls import include, path
from . import views

app_name = "music"

urlpatterns = [
# /Music/
    path('', views.IndexView.as_view(), name='index'),
# /Music/729/
    # url(r"^(?P<album_id>[0-9] + )$", view.detail, name="detail")
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),

    # #/Music/id/favorite
    # path("<int:pk>/favorite", views.favorite, name="favorite")
]