from django import forms
from .models import Career,Product,Appointment


class CareerForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = ['name', 'email', 'resume']

    def clean_resume(self):
        resume = self.cleaned_data.get('resume')
        if resume:
            if not resume.name.endswith('.pdf'):
                raise forms.ValidationError("Only PDF files are allowed.")
            if resume.size > 5 * 1024 * 1024:
                raise forms.ValidationError("File too large ( > 5MB )")
        return resume



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'details', 'image', 'subcategory']





class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'address', 'phone']
