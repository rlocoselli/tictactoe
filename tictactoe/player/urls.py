from django.conf.urls import url, include
from .views import home, new_invitation, accept_invitation
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    url(r"home$", home, name="player_home"),
    url(r"player_new_invitation$", new_invitation, name="player_new_invitation"),
    url(r"login$", LoginView.as_view(template_name="player/login_form.html"), name="player_login"),
    url(r"logout$", LogoutView.as_view(template_name="player/login_form.html"), name="player_logout"),
    url(r"accept_invitation/(?P<id>\d+)/$", accept_invitation, name="player_accept_invitation")
]