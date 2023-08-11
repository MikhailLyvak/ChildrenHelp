from datetime import timedelta
from django.contrib.auth.decorators import login_required
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
from charity.forms import HelpListForm, HelpCreateForm, HelpDetailForm


def index(request):
    """View function for the home page of the site."""
    num_helps = ReqList.objects.count()
    num_done_helps = ReqList.objects.filter(is_done=True).count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_helps": num_helps,
        "num_done_helps": num_done_helps,
        "num_visits": num_visits + 1,
    }

    return render(request, "charity/home_page.html", context=context)


class HelpListView(generic.ListView):
    model = ReqList
    context_object_name = "help_list"
    template_name = "charity/help_list.html"

    def get_queryset(self) -> QuerySet:
        queryset = ReqList.objects.filter(is_done=False)

        return queryset


class HelpMyListView(LoginRequiredMixin, generic.ListView):
    model = ReqList
    context_object_name = "help_list"
    template_name = "charity/my_help_list.html"

    def get_queryset(self) -> QuerySet:
        queryset = ReqList.objects.filter(owner=self.request.user)
        return queryset


class ReqCreateView(LoginRequiredMixin, generic.CreateView):
    model = ReqList
    form_class = HelpCreateForm
    template_name = "charity/req_create.html"
    success_url = reverse_lazy("charity:help_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ReqDetailView(LoginRequiredMixin, generic.DetailView):
    model = ReqList
    form_class = HelpDetailForm
    context_object_name = "req"
    template_name = "charity/req_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        req_user = self.request.user
        context['is_owner'] = self.request.user == self.object.owner
        context['req_user'] = req_user
        return context


@login_required
def remove_add_me_to_help(request, pk):
    req = ReqList.objects.get(pk=pk)
    if request.user in req.helpers.all():
        req.helpers.remove(request.user)
    else:
        req.helpers.add(request.user)
    return HttpResponseRedirect(reverse_lazy("charity:help_detail", args=[pk]))


@login_required
def mark_as_done(request, pk):
    req = ReqList.objects.get(pk=pk)
    if request.user == req.owner:
        req.is_done = True
        req.save()
    return HttpResponseRedirect(reverse_lazy("charity:help_detail", args=[pk]))
