from django import forms

class FeedBackForm(forms.Form):
    name=forms.CharField(
        label='Enter your Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your name'
            }
        )
    )

    rating=forms.IntegerField(
        label='Enter your  Rating',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Rating'
            }
        )
    )


    feedback=forms.CharField(
        label='Enter your Feedback',
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Your Feedback'
            }
        )
    )


