from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'size':'40'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'size':'40'}))
    phone = forms.IntegerField()
    msg_content = forms.CharField(widget=forms.Textarea, required=True)



