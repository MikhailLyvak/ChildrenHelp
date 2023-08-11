from django import forms
from charity.models import ReqList


class HelpListForm(forms.ModelForm):
    class Meta:
        model = ReqList
        exclude = ["helpers", "description"]
