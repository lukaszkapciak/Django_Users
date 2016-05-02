from django.conf.urls import url
from .views import ContactView

urlpatterns = [
    url(r'^contact/', ContactView, name='ContactView')
]