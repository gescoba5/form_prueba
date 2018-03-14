# coding=utf-8
# Se añade esta linea para poner tildes

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
  # Nombre del label del imput. La variable es la misma que se definio en el modelo
  #title = forms.CharField(label='Título')

  ''' Esto se hace para dar atributos a los campos del formulario
  def __init__(self, *args, **kwargs):
    super(PostForm, self).__init__(*args, **kwargs)
    self.fields['title'].widget.attrs = {
      'title': 'Titulo'
    }
  '''

  class Meta:
    model = Post
    fields = [
      'title',
      'text'
    ]
