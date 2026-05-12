from django import forms
from .models import Category, Advertisement, Comment
from django.core.exceptions import ValidationError

class AdForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields='__all__'
        widgets={
            'name':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'creaded_at': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),

        }
        labels={
            'title':'Nom',
            'description':'Xususiyatlar',
            'price':'Narx',
            'image':'Rasm',
            'category':'bo\'lim'
        }

    def clean_price(self):
        price=self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError("Narx manfiy bo'lmasligi kerak")
        return price


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2
            })
        }


