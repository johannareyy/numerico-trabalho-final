# This Python file uses the following encoding: utf-8

from bib import leArquivoString, organizaDados, tempQueda, transformaFloat
import matplotlib.pyplot as plt
import numpy as np

dados = open('dadosreduzidos.txt', 'r')

tabela = leArquivoString(dados)

vetorAltura, vetorMedia, vetorDesvio = organizaDados(tabela)

plt.plot([vetorAltura], [vetorMedia], "ro", label="$Dados$")

plt.errorbar(vetorAltura,vetorMedia,yerr=vetorDesvio, fmt="o-", color = 'red')

pos = np.linspace(0.5, 2.5, 100) 
plt.plot(pos, tempQueda(pos), "b-", label="$g = 9.81 m/s²$")

plt.ylabel('Tempo(s)') #descrição do y
plt.xlabel('Altura(m)') #descrição do x

plt.grid() 
plt.margins(0.1)
plt.legend()
plt.legend(loc='upper left')
plt.show()
# print(dado5.altura + dado1.altura)