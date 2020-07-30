from django import forms

class PermutationInputForm(forms.Form):
    perm_input = forms.CharField(strip=True,max_length=5,
    widget=forms.TextInput(
    attrs={'class':'form-control'})
    ,label='Permutations for') 