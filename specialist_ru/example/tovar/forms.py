from django import forms
from .models import Tovar, Tag


class TagListForm(forms.Form):
    tag_list = forms.CharField(label='новые', required=False)



class TovarForm(forms.Form):
    title = forms.CharField(label='Название', max_length=256)
    article = forms.CharField(label='Артикул', max_length=16)
    quantity = forms.IntegerField(label='В наличии', min_value=0)
    description = forms.CharField(label='Описание', widget=forms.Textarea, required=False)

class ToavrModelForm(forms.ModelForm):

    class Meta:
        model = Tovar
        fields = ['title', 'article', 'quantity', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'article': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }


class TagModelForm(forms.ModelForm):
    
    class Meta:
        model = Tag
        fields = ['title']
        widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control'})
                }
