from django import forms

class SedeFormAdmin(forms.ModelForm):
	"""docstring for SedeFormAdmin"""
	def __init__(self, *args, **kwargs):

		super(SedeFormAdmin, self).__init__(*args, **kwargs)
		self.fields['cnpj'].widget.attrs['class'] = 'mask-cnpj'
		self.fields['telefone'].widget.attrs['class'] = 'mask-telefone'
		self.fields['cep'].widget.attrs['class'] = 'mask-cep'