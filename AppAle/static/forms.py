from django import forms
class Peliculas_Formulario(forms.Form):
    titulo = forms.CharField(max_length=40)
    genero = forms.CharField(max_length=40)

class Musica_Formulario(forms.Form):
    nombre = 'models.CharField(max_length=30)'
    genero = 'models.CharField(max_length=34)'


class Hobby_Formulario(forms.Form):
    marca = 'models.CharField(max_length=30)'
    color = 'models.CharField(max_length=30)'