from django.urls import path
from .views import home, premium, ProductoDetalle, contacto, exito 
from django.http import HttpResponseRedirect
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('about/', premium, name='premium'),
    path('producto/<int:pk>/', ProductoDetalle.as_view(), name='detalle'),
    path('contacto/', contacto, name='contacto'),  # Assuming 'contacto' is a function in views.py
    path('exito/', views.exito, name='exito'),  # Redirect to 'exito' view
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)