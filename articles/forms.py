from django import forms
import datetime
from .models import Article
from django.core.exceptions import ValidationError


# class SendArticleForm(forms.Form):
#     title=forms.CharField(min_length=3 , max_length=50, error_messages={'required': 'این فیلد الزامی می باشد!!!'})
#     body=forms.CharField(widget=forms.Textarea)
#     published_at=forms.DateField()
    
    
#     def clean_published_at(self):
#         date=self.cleaned_data['published_at']
        
#         if date<datetime.date.today():
#             raise ValidationError('تاریخ ورودی نباید کوچکتر از تاریخ امروز باشد')
#         return date
    

class SendArticleForm(forms.ModelForm):
    class Meta:
        
        model = Article
        fields = ['title','body','published_at']
        
    def clean_published_at(self):
        date=self.cleaned_data['published_at']
        
        if date<datetime.datetime.today():
            raise ValidationError('تاریخ ورودی نباید کوچکتر از تاریخ امروز باشد')
        return date   