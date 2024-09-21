from django.shortcuts import render, get_object_or_404
from .models import Mood
from textblob import TextBlob  

# List of moods
def mood_list(request):
    moods = Mood.objects.all()
    return render(request, 'moods/mood_list.html', {'moods': moods})

# Details of a mood
def mood_detail(request, mood_id):
    mood = get_object_or_404(Mood, id=mood_id)
    return render(request, 'moods/mood_detail.html', {'mood': mood})

# Mood prediction based on text input
def predict_mood(request):
    mood = None
    if request.method == 'POST':
        text = request.POST.get('user_text')
        sentiment = TextBlob(text).sentiment.polarity
        if sentiment > 0:
            mood = 'happy'
        elif sentiment < 0:
            mood = 'sad'
        else:
            mood = 'neutral'
    return render(request, 'moods/predict.html', {'mood': mood})
