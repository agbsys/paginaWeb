from django import forms

class formularioContacto(forms.Form):
    nombre=forms.CharField(label="Nombre", required=True)
    email=forms.EmailField(label="Correo", required=True)
    mensaje=forms.CharField(label="Comentario", required=True, widget=forms.Textarea)