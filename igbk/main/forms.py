from django import forms


class KeysWordsForm(forms.Form):
    keys_words = forms.CharField(label='keys_words', max_length=100)
