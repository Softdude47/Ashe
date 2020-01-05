from django import forms

'''class CommentForm(forms.Form):
    user_name = forms.CharField(max_length=100)
    email_address = forms.EmailField()
    full_name = forms.CharField(max_length=30)
    password = forms.CharField(max_length=100)
    image = forms.ImageField(upload_to='pic')'''

class Profile_Picture_Form(forms.Form):
    image = forms.ImageField(max_length=100, label='image')
    user_name = forms.CharField(max_length=100, required=True)

class CommentsForm(forms.Form):
    text = forms.CharField(label='comment', max_length=2000, widget=forms.Textarea({'width': '100%', 'col': '30', 'row': '50'}))
    posted_by = forms.CharField(max_length=200, widget=forms.HiddenInput())
    time = forms.DateTimeField(input_formats='d/m/Y', widget=forms.HiddenInput())