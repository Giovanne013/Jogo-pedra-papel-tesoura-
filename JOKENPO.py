# 1- opçoes de jogadas. pedra papel, tesoura.
# 2- escolha do jogador qual ele vai jogar
# 3- escolha do computador joga, aleatoriamente.
# 4- definir quem vai ganhar
# 5- mostrar quem venceu.
import random
print('[1]PEDRA\n[2]PAPEL\n[3]TESOURA')
jogada_human = str(input('sua jogada: ')).upper()#jogandos todas as letras para maiuscula para não ter erro de digitação na hora de jogar
jogada_computer = ['PEDRA','PAPEL','TESOURA']#criando lista 
embaralhar_jogada = random.choice(jogada_computer)#embaralhando a lista com o choice
print("Computador jogou: ",embaralhar_jogada)

#logica para para resultados
if jogada_human == embaralhar_jogada:
    print('\033[31mJogo empatado!\033[0m')

elif jogada_human == "PEDRA" and embaralhar_jogada == "TESOURA" :
    print("\033[31mVocê Ganhou!\033[0m")

elif jogada_human == "PAPEL" and embaralhar_jogada == "PEDRA" :
    print("Você Ganhou!")

elif jogada_human == "TESOURA" and embaralhar_jogada == "PAPEL":
    print("Você Ganhou!")

else:
    print("O computador ganhou!")