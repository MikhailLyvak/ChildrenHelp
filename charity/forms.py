from django import forms
from charity.models import ReqList


class HelpListForm(forms.ModelForm):
    class Meta:
        model = ReqList
        exclude = ["helpers", "description"]


class HelpCreateForm(forms.ModelForm):
    class Meta:
        model = ReqList
        exclude = ["helpers", "owner", "date", "is_done"]
        

class HelpDetailForm(forms.ModelForm):
    class Meta:
        model = ReqList
        exclude = ["is_done", ]
