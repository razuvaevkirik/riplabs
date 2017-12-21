from django.conf.urls import url
from . import views
from app.views import TicketView

urlpatterns = [
    url(r'^(?P<id>\d+)', TicketView.as_view(), name='ticket_url'),
]
