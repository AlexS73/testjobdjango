from django.forms import ModelForm
from django import forms
from .models import Recruit, ResultTest

class RecruitForm(ModelForm):
    class Meta:
        model = Recruit
        fields = ('name','planet','email','age')


class ResultTestForm(forms.Form):
    question = forms.CharField(max_length=500)
    choise = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class':'Radio'}),
                                choices=(('Да','Да'),('Нет','Нет')))

    def save(self, ownrecruit = None):
        new_result = ResultTest.objects.create(
            recruit = ownrecruit,
            question = self.cleaned_data['question'],
            choise = self.cleaned_data['choise']
        )
        return new_result