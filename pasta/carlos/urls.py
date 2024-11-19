from django.urls import path
from carlos import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name='home'),
    path('sobre',views.sobre,name='sobre'),
    path('contado',views.contado,name='contado'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
