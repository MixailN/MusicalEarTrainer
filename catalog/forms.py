from django import forms

NOTE_CHOICES = [('1', 'd#3'), ('2', 'd3'), ('3', 'c3')]


class AnswerForm(forms.Form):
    answer_list = forms.ChoiceField(widget=forms.RadioSelect, choices=NOTE_CHOICES)

