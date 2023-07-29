from django.urls import path

from nice_a.common.views import index, like_photo, share_photo, comment_photo

urlpatterns = (
    path('', index, name='index'),
    path('like/<int:photo_id>/', like_photo, name='like_photo'),
    path('share/<int:photo_id>/', share_photo, name='share_photo'),
    path('comment/<int:photo_id>/', comment_photo, name='comment_photo'),
)