import math
import os

vdd = True
#evitar que o usuário digite algo que não foi solicitado
while vdd:
  os.system("clear||cls")
  print("Calculador de Média, Variância e Desvio-Padrão.\n")
  inicia = input("Deseja iniciar o programa? (S/N):").upper()
  if inicia != "S" and inicia != "N":
      input("Por favor digite S ou N!")
  elif inicia == "N":
      print("\nPrograma encerrado!")
      vdd = False
  else:
      while inicia == "S":
          vdd = True
          while vdd:
              #evitar que ele escreva outro tipo
              try:
                  q = int(input("\nQuantos números são? "))
                  vdd = False
              except ValueError:
                  print("Digite um número válido!")
          #contador para somar todos os números para poder realizar a média
          soma = 0
          #armazenar o desvio padrão de cada número
          l = []
          #mesmo princípio da soma
          vari = 0
          for i in range(q):
              vdd=True
              while vdd:
                  try:
                      n = float(input(f"Digite o {i + 1}º número: "))
                      vdd=False
                  except ValueError:
                      print("Digite um número válido.")
                  soma += n
              l.append(n)
          media = soma / q
          for j in l:
              #calculo da variancia
              vari += (j - media) ** 2
          variancia = vari / q
          #biblioteca do math para calcular a raiz
          desvio = math.sqrt(variancia)
          print("A média dos números digitados é  %.2f:" %media)
          print("A variância dos números digitados é: %.2f" %variancia)
          print("O desvio-padrão é %.2f" % desvio)
          inicia = input("Deseja continuar ? (S/N):").upper()
          if inicia == "N":
              print("\nPrograma Encerrado!")