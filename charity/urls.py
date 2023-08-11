from django.urls import path
from charity.views import (
    HelpListView,
    ReqCreateView,
    ReqDetailView,
    HelpMyListView,
    remove_add_me_to_help,
    mark_as_done,
    index
)


urlpatterns = [
    path("home/", index, name="home"),
    path("help_list/", HelpListView.as_view(), name="help_list"),
    path("myhelp_list/", HelpMyListView.as_view(), name="myhelp_list"),
    path("help_list/create/", ReqCreateView.as_view(), name="help_create"),
    path("help_list/<int:pk>/", ReqDetailView.as_view(), name="help_detail"),
    path("help_list/<int:pk>/remove_add_me_to_help/",
        remove_add_me_to_help, name="remove-add-me-to-help"
    ),
    path("help_list/<int:pk>/mark_as_done/",
        mark_as_done, name="mark-ass-done"
    ),
]

app_name = "charity"
