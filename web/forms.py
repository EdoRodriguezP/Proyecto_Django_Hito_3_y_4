from django import forms

class Contacto_Formulario(forms.Form):
    customer_email = forms.EmailField(label='Email', max_length=254, required=True, widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg'}))
    customer_name = forms.CharField(label='Nombre', max_length=64, required=True, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    customer_message = forms.CharField(label='Mensaje', required=True, widget=forms.Textarea(attrs={'class': 'form-control form-control-lg'}))

    def clean_customer_email(self):
        email = self.cleaned_data.get('customer_email')
        if not email:
            raise forms.ValidationError("Este campo es obligatorio.")
        return email

    def clean_customer_name(self):
        name = self.cleaned_data.get('customer_name')
        if not name:
            raise forms.ValidationError("Este campo es obligatorio.")
        return name

    def clean_customer_message(self):
        message = self.cleaned_data.get('customer_message')
        if not message:
            raise forms.ValidationError("Este campo es obligatorio.")
        return message