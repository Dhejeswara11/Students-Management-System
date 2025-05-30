from django import forms


class StockForm(forms.Form):
    
    name = forms.CharField(max_length=25,
                                  widget=forms.TextInput(attrs={"class": "form-control"}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))
    quantity= forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))

    categoryId = forms.ChoiceField(choices=[],
                                   widget=forms.Select(attrs={"class": "form-control"}))


