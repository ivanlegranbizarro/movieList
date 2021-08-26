from django.urls import path
from watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamingPlatformAV, StreamingPlatformDetailAV, \
    ReviewList, ReviewDetail

# from watchlist_app.api.views import movie_list, movie_details

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-details'),
    path('stream/', StreamingPlatformAV.as_view(), name='stream-platform'),
    path('stream/<int:pk>/', StreamingPlatformDetailAV.as_view(), name='stream-detail'),
    path('stream/<int:pk>/review/', StreamingPlatformDetailAV.as_view(), name='stream-detail'),
    path('stream/review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    # path('list/', movie_list, name='movie-list'),
    # path('<int:pk>/', movie_details, name='movie-details')
]
