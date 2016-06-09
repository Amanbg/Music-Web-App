from django.conf.urls import url
from tracks.views import TrackListView, TrackDetailView, GenreListView, GenreDetailView
from . import views
urlpatterns = [

    url(r'^tracks/$', view=TrackListView.as_view(), name='track-view'),
    url(r'^track/$', views.EditTrack, name='track-edit-view'),
    url(r'^track/(?P<pk>\d+)/$', view=TrackDetailView.as_view(), name='trackdetail-view'),
    url(r'^genres/$', view=GenreListView.as_view(), name='genre-view'),
    url(r'^genres/(?P<pk>\d+)/$', view=GenreDetailView.as_view(), name='genredetail-view'),
    url(r'^search/$', views.SearchView, name='searchbarview'),
]
