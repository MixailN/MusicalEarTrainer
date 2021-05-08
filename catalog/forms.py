from django import forms

NOTE_CHOICES = [('1', 'd#3'), ('2', 'd3'), ('3', 'c3')]


class AnswerForm(forms.Form):
    answer_list = forms.ChoiceField(widget=forms.RadioSelect)

    def __init__(self, note_choices, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['answer_list'].choices = note_choices
