#! /usr/bin/python3
# -*- coding: utf-8 -*-
#
# Algoritmos para ajuste de funções
#_________________________________________________________
# Universidade Federal de Santa Catarina
# Departamento de Engenharias da Mobilidade
# Curso de Cálculo Numérico
# Prof. Alexandre Zabot
# https://zabot.paginas.ufsc.br
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
import math
import numpy as np




def reta(x,y,verbose=True):
  """
  Descrição:
    Ajusta uma reta (y = a0 + a1*x) em um conjunto de dados {x,y}
  Recebe:
    {x,y}   => Pontos
    verbose => Imprime passo a passo da conta
  Retorna:
    Coeficientes a,b da reta 
  """

  # Verificações
  N = len(x)
  assert len(y)==N, "x e y têm tamanhos diferentes"
  
  # Somatórios
  sx  = 0
  sx2 = 0
  sy  = 0
  sxy = 0
  for i in range(N):
    sx  += x[i]
    sx2 += x[i]*x[i]  
    sy  += y[i]
    sxy += x[i]*y[i]
  
  # Coeficientes
  den = N*sx2 - sx*sx
  a0  = (sx2*sy - sxy*sx)/float(den)
  a1  = (N*sxy - sx*sy)/float(den)


  if verbose:
    print("------------------------------")
    print("Somas:")
    print("  Soma x_i     = ",sx)
    print("  Soma x_i^2   = ",sx2)
    print("  Soma y_i     = ",sy)
    print("  Soma x_i*y_i = ",sxy)
    print("Reta ajustada: y = a0 + a1*x")
    print("  a0 = ",a0)
    print("  a1 = ",a1)
 
  return a0,a1




def polinomio(x,y,g,verbose=True):
  """
  Descrição:
    Ajusta um polinômio de grau g em um conjunto de dados {x,y}
  Recebe:
    {x,y}   => Pontos
    g       => Grau do polinômio
    verbose => Imprime passo a passo da conta
  Retorna:
    Vetor com os g+1 coeficientes do polinômio
  """

  # Verificações
  N = len(x)
  assert len(y)==N, "x e y têm tamanhos diferentes"
  assert g>0, "grau inválido para o polinômio"
  n = g+1
  
  
  # Monta as matrizes
  sx  = np.zeros(2*g+1)
  sxy = np.zeros(n)
  for i in range(N):
    xn = 1.0
    for j in range(2*g+1):
      sx[j]  += xn
      if j<g+1:
        sxy[j] += y[i]*xn
      xn *= x[i]
  
  A = np.zeros( (n,n) )
  B = np.zeros( n )
  for i in range(n):
    for j in range(n):
      A[i][j] = sx[i+j]
    B[i] = sxy[i]



  # Mostro a matriz aumentada
  if verbose:
    print("------------------------------")
    print("Matriz aumentada:")
    for i in range(n):
      for j in range(n):
        print("{:12.6g}".format(A[i][j]),end="")
      print(" | %12.6g" % B[i])



  # Resolve o sistema linear e obtém os coeficientes
  a = np.linalg.solve(A,B)
  if verbose:
    print("------------------------------")
    print("Coeficientes do Polinômio:")
    print("a = ",a)
 
  return a




def potencia(x,y,verbose=True):
  """
  Descrição:
    Ajusta uma Lei de Potência (y = b*x^a) em um conjunto de dados {x,y}
  Recebe:
    {x,y}   => Pontos
    verbose => Imprime passo a passo da conta
  Retorna:
    Coeficientes a,b da Lei de Potência
  """
  
  # Verificações
  N = len(x)
  assert len(y)==N, "x e y têm tamanhos diferentes"

  
  X = np.log(x)
  Y = np.log(y)


  B,a = reta( X, Y, verbose )
  b = np.exp(B)
  
  
  if verbose:
    print("------------------------------")
    print("Ajuste de Lei de Potência: y = b x^a"    )
    print("------------------------------")
    print("Dados:")
    print("   x   |   y   |   ln x   |   ln y   ")
    for i in range(N):
      print("  %6.3f |  %6.3f |  %6.3f |  %6.3f |" % (x[i],y[i],X[i],Y[i]))
    
    print("\n\n------------------------------")
    print("Coeficientes ajustados:")
    print("B = ",B)
    print("b = exp(B) = ",b)
    print("a = ",a)
    print("------------------------------")
    print("Ajuste de Lei de Potência: y = %.3g x^%.3g" % (b,a)    )
  
  
  return a,b




def exponencial(x,y,verbose=True):
  """
  Descrição:
    Ajusta uma Lei Exponencial (y = b*exp(ax)) em um conjunto de dados {x,y}
  Recebe:
    {x,y}   => Pontos
    verbose => Imprime passo a passo da conta
  Retorna:
    Coeficientes a,b da Lei de Potência
  """
  
  # Verificações
  N = len(x)
  assert len(y)==N, "x e y têm tamanhos diferentes"

  
  Y = np.log(y)


  B,a = reta( x, Y, verbose )
  b = np.exp(B)
  
  
  
  if verbose:
    print("------------------------------")
    print("Dados:")
    print("   x   |   y   |   ln y   ")
    for i in range(N):
      print("  %6.3f |  %6.3f |  %6.3f |" % (x[i],y[i],Y[i]))
    
    print("\n\n------------------------------")
    print("Coeficientes ajustados:")
    print("B = ",B)
    print("b = exp(B) = ",b)
    print("a = ",a)
    print("------------------------------")
    print("Ajuste de Exponencial: y = %.3g * exp(%.3g * x)" % (b,a)    )

  
  return a,b    
    
  
  


  
  
  
  
  
  
  
  
  
  

