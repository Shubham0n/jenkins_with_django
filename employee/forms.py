from django import forms
from .models import EmployProfile

class EmployProfileForm(forms.ModelForm):
    class Meta:
        model = EmployProfile
        fields = [
            "name",
            "email",
            "phone_number",
            "linkedin",
            "github",
            "objective",
            "address",
            "total_experience",
        ] 
