from django import forms
from .models import *

class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'

class ProductSubCategory(forms.ModelForm):
    class Meta:
        model = ProductSubCategory
        fields = '__all__'

class ProductInformationForm(forms.ModelForm):
    class Meta:
        model = ProductInformation
        fields = '__all__'

class ProductImagesForm(forms.ModelForm):
    class Meta:
        model = ProductImages
        fields = '__all__'