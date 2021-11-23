from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('',main_view,name="Home")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
