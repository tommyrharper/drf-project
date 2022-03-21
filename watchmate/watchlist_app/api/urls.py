from django.urls import path

# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import (
    WatchListAV,
    WatchListDetailAV,
    StreamPlatformAV,
    StreamPlatformDetailAV,
)

## method based urls
# urlpatterns = [
#     path("list/", movie_list, name="movie-list"),
#     path("<int:pk>/", movie_details, name="movie-detail"),
# ]

urlpatterns = [
    path("list/", WatchListAV.as_view(), name="movie-list"),
    path("<int:pk>/", WatchListDetailAV.as_view(), name="movie-detail"),
    path("stream/", StreamPlatformAV.as_view(), name="platform-list"),
    path("stream/<int:pk>/", StreamPlatformDetailAV.as_view(), name="platform-detail"),
]
