#def cria a função

def receber_inteiro(mensagem):
	valor = input(mensagem)
	if valor.isnumeric():
		return valor
	print('Número inválido')
	exit()

	usuario = {
	'nome': input('Digite seu nome: '),
	'idade': receber_inteiro('Digite sua idade: '),
	'peso': receber_inteiro('Digite seu peso: '),

	}

#recriando a função

def receber_inteiro2(mensagem):
	valor = ''
	while not valor.isnumeric():
		valor = input(mensagem)
	return int (valor)

	usuario = {
	'nome': input('Digite seu nome: '),
	'idade': receber_inteiro2('Digite sua idade: '),
	'peso': receber_inteiro2('Digite seu peso: '),
	
	print(usuario)

}

