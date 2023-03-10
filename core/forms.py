from django import forms

class ClientesFormAdmin(forms.ModelForm):
	"""docstring for ClientesFormAdmin"""
	def __init__(self, *args, **kwargs):

		super(ClientesFormAdmin, self).__init__(*args, **kwargs)
		self.fields['cpf'].widget.attrs['class'] = 'mask-cpf'
		# self.fields['data_de_nascimento'].widget.attrs['class'] = 'mask-data'
		self.fields['telefone'].widget.attrs['class'] = 'mask-telefone'
		self.fields['cep'].widget.attrs['class'] = 'mask-cep'
		self.fields['telefone_contato'].widget.attrs['class'] = 'mask-telefone'

class ContratosFormAdmin(forms.ModelForm):
	"""docstring for ContratosFormAdmin"""
	def __init__(self, *args, **kwargs):

		super(ContratosFormAdmin, self).__init__(*args, **kwargs)
		self.fields['valor'].widget.attrs['class'] = 'mask-money'
		self.fields['taxa'].widget.attrs['class'] = 'mask-money'
		self.fields['valor_entrada'].widget.attrs['class'] = 'mask-money'
		