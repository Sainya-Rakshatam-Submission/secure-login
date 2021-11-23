from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path, re_path

from . import views

urlpatterns = [
    url(r"^login/$", views.loginform, name="signin"),
    url(r"^logout/$", views.user_logout, name="signout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)