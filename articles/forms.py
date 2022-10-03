from django import forms



class SendArticleForm(forms.Form):
    title=forms.CharField()
    body=forms.CharField(widget=forms.Textarea)
    published_at=forms.DateTimeField()