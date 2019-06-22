
MENSAGEM = 'Digite o número de avaliações:'

	numero_de_avaliacoes = input(MENSAGEM)
	if not numero_de_avaliacoes.isnumeric():
	print('Número inválido')
	numero_de_avaliacoes = int(numero_de_avaliacoes)

	lista_de_avaliacoes = []

	for i in range(numero_de_avaliacoes):
	nota = input('Digite a nota: ')
	if not nota.isnumeric():
	print('Número invalido')
		exit()
			nota = int(nota)
			lista_de_avaliacoes.append(nota)
			media = sum(lista_de_avaliacoes) / numero_de_avaliacoes

if media>= 6:
	print('Aprovado com média {}'.format(media))
else:
	print('Reprovado com média {}'.format(media))


