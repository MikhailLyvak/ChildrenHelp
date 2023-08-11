from django.urls import path
from charity.views import HelpListView


urlpatterns = [
    path('help_list/', HelpListView.as_view(), name='help_list'),
]

app_name = "charity"