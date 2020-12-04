# This Python file uses the following encoding: utf-8

from bib import leArquivoString, organizaDados, tempQueda, transformaFloat, ajusteFuncao, log10
import matplotlib.pyplot as plt
import numpy as np
import math

#Leitura e organização de dados
dados = open('dadosreduzidos.txt', 'r')
tabela = leArquivoString(dados)
vetorAltura, vetorMedia, vetorDesvio = organizaDados(tabela)

# # -----------------------------------------------------------------------------------------
# #Linearização 1

x = np.power(vetorMedia,2)
y = vetorAltura
a0,a1 = ajusteFuncao(x, y)
g = 2*a1

print(" coeficiente linear deveria ser 0, ficou sendo ", a0)
print(" g deveria ser 9.8, ficou sendo: ", g)

# -----------------------------------------------------------------------------------------
# Linearização 2

# x = log10(np.sqrt(vetorAltura))
# y = np.log10(vetorMedia)
# a0,a1 = ajusteFuncao(x, y)
# g = 2/pow(10,2*a0)

# print(" coeficiente linear deveria ser 1, ficou sendo ", a1)
# print(" g deveria ser 9.8, ficou sendo: ", g)


# -----------------------------------------------------------------------------------------
#Gráfico

plt.plot(vetorAltura, vetorMedia, "ro")
plt.errorbar(vetorAltura,vetorMedia,yerr=vetorDesvio, fmt="o-", color = 'red', label="$Dados$")

pos = np.linspace(0.5, 2.5, 100) 
plt.plot(pos, tempQueda(pos, 9.81), "b-", label="$g = 9.81 m/s²$")

posAjustada = np.linspace(0.5, 2.5, 100)
plt.plot(posAjustada, tempQueda(posAjustada, g), "y-", label="$Ajuste$")

#Config do gráfico
plt.ylabel('Tempo(s)') #descrição do y
plt.xlabel('Altura(m)') #descrição do x

plt.grid() 
plt.margins(0.1)
plt.legend()
plt.legend(loc='upper left')
plt.show()