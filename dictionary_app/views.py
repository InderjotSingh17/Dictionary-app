import requests
from django.shortcuts import render
from .models import Word

def get_word_meaning(request):
    word = request.GET.get('word', '') 

    api_url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    meaning = None
    error = None
    if word:
        response = requests.get(api_url)
        if response.status_code == 200:
            meaning= response.json() 
            Word.objects.create(word=word,meaning=meaning)
            print(f"Word '{word}' saved successfully!")
        else:
            error = "Word not found or API error."
    return render(request, 'home.html', {'word': word, 'meaning': meaning,'error': error})
