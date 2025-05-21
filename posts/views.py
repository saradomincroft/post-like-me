import requests
from django.shortcuts import render
from .forms import PostInputForm

AZURE_FUNCTION_URL = "https://your-azure-function-url.azurewebsites.net/api/your-function-name?code=your-function-key"

def generate_post(request):
    result = None
    if request.method == 'POST':
        form = PostInputForm(request.POST)
        if form.is_valid():
            posts = form.cleaned_data['past_posts'].split('\n')
            topic = form.cleaned_data['topic']
            response = request.post(AZURE_FUNCTION_URL, json={
                "posts": posts,
                "topic": topic
            })
            result = response.text
        else:
            form = PostInputForm()
        return render(request, 'posts/form.html', {'form': form, 'result': result})