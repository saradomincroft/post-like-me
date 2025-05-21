from django import forms

class PostInputForm(forms.Form):
    post_posts = forms.CharField(widget=forms.Textarea, help_text="Enter your posts here.")
    topic = forms.charField(max_length=100, help_text="Enter the topic of your post.")