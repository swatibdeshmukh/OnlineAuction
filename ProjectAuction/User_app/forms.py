from django import forms
from .models import *

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        field = '__all__'

class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = '__all__'

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = '__all__'

class IdProofForm(forms.ModelForm):
    class Meta:
        model = IdProof
        fields = '__all__'