from django.shortcuts import render

from .forms import KeysWordsForm


def index(request):
    if request.method == 'POST':
        form = KeysWordsForm(request.POST)
        if form.is_valid():
            return render(request, 'main/done.html', {'keys_words': form.cleaned_data['keys_words']})
    else:
        form = KeysWordsForm()
    return render(request, template_name='main/index.html', context={'form': form})
