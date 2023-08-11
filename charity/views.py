from datetime import timedelta
from typing import Any, Dict
from datetime import date
from django.db.models.query import QuerySet
from django.utils import timezone
from django.utils.timezone import now
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, Http404

from charity.models import ReqList
from charity.forms import HelpListForm


class HelpListView(generic.ListView):
    model = ReqList
    context_object_name = "help_list"
    template_name = "charity/help_list.html"
