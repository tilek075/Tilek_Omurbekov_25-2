from django import forms


class ProductCreateForm(forms.Form):
    image = forms.FileField(required=False)
    title = forms.CharField(max_length=255)
    model = forms.CharField(max_length=255)
    specification = forms.CharField(widget=forms.Textarea())
    description = forms.CharField(widget=forms.Textarea())
    price = forms.IntegerField()


class ReviewCreateForm(forms.Form):
    text = forms.CharField(max_length=355)
