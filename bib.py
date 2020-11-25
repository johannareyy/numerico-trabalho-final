
import matplotlib.pyplot as plt
import numpy as np


def log10(x):
    return np.log(x)

def ajusteFuncao (vetorAltura, vetorMedia):
    """Faz um ajuste de função pelo método dos mínimos quadrados.
    Recebe: Conjunto de valores {h,t}.
    Retorna: Coeficientes a0 e a1 da reta.
    """
    somaAltura = 0
    somaMedia = 0
    somaAlturaMedia = 0
    somaAlturaQuadrado = 0

    for i in range(5):
        somaAltura += vetorAltura[i]
        somaMedia += vetorMedia[i]
        somaAlturaQuadrado += pow(vetorAltura[i],2)
        somaAlturaMedia += vetorAltura[i]*vetorMedia[i]
    
    a0 = (somaAlturaQuadrado*somaMedia - somaAlturaMedia*somaAltura)/(5*somaAlturaQuadrado - pow(somaAltura,2))

    a1 = (5*somaAlturaMedia - somaAltura*somaMedia)/(5*somaAlturaQuadrado - pow(somaAltura,2))


    return a0, a1

def transformaFloat(vetorAltura, vetorMedia, vetorDesvio):
    """transforma um vetor de strings em um vetor de floats.
    Recebe = 3 vetores de strings.
    Retorna = 3 vetores de floats.
    """
    cont = 0
    for x in vetorAltura:
        vetorAltura[cont] = float(x)
        cont += 1

    cont = 0
    for x in vetorMedia:
        vetorMedia[cont] = float(x)
        cont += 1
        
    cont = 0
    for x in vetorDesvio:
        vetorDesvio[cont] = float(x)
        cont += 1

    return vetorAltura, vetorMedia, vetorDesvio


def leArquivoString (dados):
    """Lê um arquivo e devolve um vetor com cada linha em uma posição.
    Recebe: arquivo em txt.
    Retorna: vetor com dados do arquivo.
    """
    tabela=[] 
    tabela.append(dados.readline()) #lê linha por linha do arquivo e armazena em um vetor
    tabela.append(dados.readline())
    tabela.append(dados.readline())
    tabela.append(dados.readline())
    tabela.append(dados.readline())

    return tabela


def organizaDados (tabela):
    """Organiza os dados do arquivo recebidos em 3 vetores, e depois chama função transformaFloat.
    Recebe: vetor com cada dado da linha por posição do vetor em tipo string.
    Retorna: 3 vetores com dados separados como tipo float.
    """
    vetorAltura = []
    vetorMedia = []
    vetorDesvio = []
    linha = 0

    for y in tabela:
        auxpipe = 0
        auxprimeirocaracter = True
        for x in y:
            if x != '|':
                if auxpipe == 0:
                    if auxprimeirocaracter == True:
                        vetorAltura.append(x)
                        auxprimeirocaracter = False
                    else:
                        vetorAltura[linha] += x
                if auxpipe == 1:
                    if auxprimeirocaracter == True:
                        vetorMedia.append(x)
                        auxprimeirocaracter = False
                    else:
                        vetorMedia[linha] += x
                if auxpipe == 2:
                    if auxprimeirocaracter == True:
                        vetorDesvio.append(x)
                        auxprimeirocaracter = False
                    else:
                        vetorDesvio[linha] += x
            elif x == '|':
                auxpipe += 1
                auxprimeirocaracter = True
        linha += 1
    contador = 0
    for i in vetorDesvio:
        vetorDesvio[contador] = i.replace('\n', '')
        contador += 1

    vetorAltura, vetorMedia, vetorDesvio = transformaFloat(vetorAltura, vetorMedia, vetorDesvio)

    return vetorAltura, vetorMedia, vetorDesvio


def tempQueda (pos, g):
    """
    Calcula o tempo de queda livre para dada posição.

    Recebe: posição inicial.

    Retorna: tempo de queda.
    """
    return (2*pos/g)**(1/2)
