from django.conf.urls import url
from .views import ContactView

urlpatterns = [
    url(r'', ContactView, name='ContactView')
]