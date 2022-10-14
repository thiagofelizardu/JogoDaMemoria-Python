import random

# Constantes 
CARTAS = ["Java  ", "Python", "C++   ","PHP   ", "Java  ", "Python", "C++   ","PHP   "]
CARTA_VIRADA = "******"
LINHAS = 2
COLUNAS = 4

# Cria e retorna uma nova lista que é a
# cópia da lista passada como parâmetro
def obterCopia(lista):
    copia = []
    for k in lista:
        copia.append(k)
    return copia

# Retorna uma nova lista misturando a ordem
# dos elementos
def obterListaMisturada(lista):
    copia = obterCopia(lista)
    random.shuffle(copia)
    return copia

# Cria um tabuleiro com a quantidade
# de linhas e colunas e onde em cada
# posição está o valor de CARTA_VIRADA
def obterNovoTabuleiro():
    lista = []
    for y in range(LINHAS):
        linha = []
        for x in range(COLUNAS):
            linha.append(CARTA_VIRADA)
        lista.append(linha)
    return lista    

# Obtém um tabuleiro (matriz) montado
# misturando as posições da lista de CARTAS
def montarTabuleiro():
    tabuleiro = obterNovoTabuleiro()
    cartasMisturadas = obterListaMisturada(CARTAS)
    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            carta = cartasMisturadas.pop()
            tabuleiro[linha][coluna] = carta
    return tabuleiro

# Imprime na tela o tabuleiro
def imprimeTabuleiro(tabuleiro):
    print("="*35)
    for x in range(LINHAS):
        linha = ""
        for y in range(COLUNAS):
            linha+=tabuleiro[x][y] + "   "
        print(linha)
    print("="*35)
    print()

# Verifica se todas as cartas já foram descobertas
# retornando False caso alguma carta ainda esteja
# virada.
def descobriuTodas(tabuleiroMostrado):
    for x in range(LINHAS):
        linha = ""
        for y in range(COLUNAS):
            if (tabuleiroMostrado[x][y] == CARTA_VIRADA):
                return False
    return True

    
#PROGRAMA PRINCIPAL
tabuleiro = montarTabuleiro()
tabuleiroMostrado = obterNovoTabuleiro()
numTentativas = 0
while(True):
    numTentativas+=1
    linha1 = int(input("Escolha o número da linha [0,1]"))
    coluna1 = int(input("Escolha o número da coluna [0,3]"))
    tabuleiroMostrado [linha1][coluna1] = tabuleiro  [linha1][coluna1]
    imprimeTabuleiro(tabuleiroMostrado)
    linha2 = int(input("Escolha o número da linha [0,1]"))
    coluna2 = int(input("Escolha o número da coluna [0,3]"))
    tabuleiroMostrado [linha2][coluna2] = tabuleiro  [linha2][coluna2]
    imprimeTabuleiro(tabuleiroMostrado)
    if (tabuleiro  [linha1][coluna1] != tabuleiro[linha2][coluna2]):
        print("Diferentes... Tente novamente")
        tabuleiroMostrado [linha1][coluna1] = CARTA_VIRADA
        tabuleiroMostrado [linha2][coluna2] = CARTA_VIRADA
        imprimeTabuleiro(tabuleiroMostrado)
    else:
        print("Acertou o par! Parabéns!")
    if (descobriuTodas(tabuleiroMostrado)==True):
        print("Parabéns! Você conseguiu! Tentativas:", numTentativas)
        break
imprimeTabuleiro(tabuleiro)

print("Game Over")