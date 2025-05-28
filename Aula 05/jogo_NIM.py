def main():
	inicio = 0
	while inicio != 1 and inicio != 2:
		print("Bem vindo ao jogo NIM! Escolha: ")
		print("1 - para jogar uma partida isolada")
		print("2 - para jogar um campeonado")
		inicio = int(input())
		print()
		if inicio != 1 and inicio != 2:
			print("Opção inválida!")
			print()
		if inicio == 1:
			print("Você escolheu uma partida!")
			print()
			partida()
		if inicio == 2:
			print("Você escolheu um campeonato!")
			print()
			campeonato()
		

def partida():
	n = int(input("Quantas peças? "))
	m = int(input("Limite de peças por jogada? "))
	
	while m > n: 
		print("Limite de peças inválido!")
		n = int(input("Quantas peças? "))
		m = int(input("Limite de peças por jogada? "))
		
	if n % (m+1) == 0:
		print("Você começa!")
		print()
		vez = 1
	else:
		print("Computador começa!")
		print()
		vez = 0
	while n > 0:
		if vez == 0:
			jogada_computador = computador_escolhe_jogada(n,m)
			n = n - jogada_computador
			print("Computador tira ", jogada_computador, "peças")
			print("Quantidade de peças que restaram: ", n)
			print()
			vez = 1 
		else :
			jogada_usuario = usuario_escolhe_jogada(n,m)
			n = n - jogada_usuario
			print("Jogador tira ", jogada_usuario, "peças")
			print("Quantidade de peças que restaram: ", n)
			print()
			vez = 0 
	if vez == 0:
		print("Fim do jogo! Você venceu!")
		print()
	if vez == 1:
		print("Fim do jogo! O computador venceu!")
		print()
	return(vez)

def campeonato():
	rodada = 1
	pontos_computador = 0
	pontos_usuario =0
	while pontos_computador < 3 and pontos_usuario < 3:
		print("**** Rodada ", rodada, " ****")
		print()
		vencedor = partida()
		if vencedor == 0:
			pontos_usuario = pontos_usuario + 1
		if vencedor == 1: 
			pontos_computador = pontos_computador + 1
		rodada = rodada + 1
	print("**** Final do campeonato ****")
	print()
	print("Placar: Você", pontos_usuario, "X", pontos_computador, "Computador")
	
def computador_escolhe_jogada(n,m):
	jogada = 1 
	while jogada != m:
		if (n - jogada)%(m+1) == 0:
			return (jogada)
		else:
			jogada = jogada + 1
	return (jogada)


def usuario_escolhe_jogada(n,m):
	jogada = int(input("Quantas peças você deseja tirar? "))
	while jogada > m or jogada == 0:
		print("Jogada inválida!")
		jogada = int(input("Quantas peças você deseja tirar? "))
	return (jogada)
					
main()
