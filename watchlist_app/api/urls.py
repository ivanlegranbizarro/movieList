from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import StreamPlatformViewSet, WatchListAV, WatchDetailAV, StreamingPlatformAV, StreamingPlatformDetailAV, \
    ReviewList, ReviewDetail, ReviewCreate

router = DefaultRouter()
router.register('router-movie', StreamPlatformViewSet,
                basename='router-movie')

# from watchlist_app.api.views import movie_list, movie_details

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-details'),
    path('stream/', StreamingPlatformAV.as_view(), name='stream-platform'),
    path('stream/<int:pk>/', StreamingPlatformDetailAV.as_view(),
         name='stream-detail'),
    path('<int:pk>/review/',
         ReviewList.as_view(), name='review-list'),
    path('<int:pk>/review-create/',
         ReviewCreate.as_view(), name='review-create'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    path('', include(router.urls))
]
