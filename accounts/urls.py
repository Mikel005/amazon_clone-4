from django.urls import path
from . import views
# from .views import signup_view


urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    # path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]