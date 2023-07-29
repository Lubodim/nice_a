# accounts/urls.py
from django.urls import path, include

from nice_a.accounts.views import login_user, register_user, details_user, delete_user, edit_user

urlpatterns = (
    path('login/', login_user, name='login_user'),
    path('register/', register_user, name='register_user'),
    path('profile/<int:pk>/', include([
        path('', details_user, name='details_user'),
        path('delete/', delete_user, name='delete_user'),
        path('edit/', edit_user, name='edit_user'),
    ])),

)
