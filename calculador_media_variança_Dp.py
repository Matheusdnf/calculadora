import math

print("Calculador de Média, Variância e Desvio-Padrão.\n")

vdd = True
while vdd:
    inicia = input("Deseja iniciar o programa? (S/N):").upper()
    if inicia != "S" and inicia != "N":
        print("Por favor digite S ou N!")
    elif inicia == "N":
        print("Programa encerrado!")
        vdd = False
    else:
        while inicia == "S":
            vdd = True  # Reset vdd for the number of values input
            while vdd:
                try:
                    q = int(input("\nQuantos números são? "))
                    vdd = False
                except ValueError:
                    print("Digite um número válido!")
            soma = 0
            l = []
            vari = 0
            for i in range(q):
                while True:
                    try:
                        n = float(input(f"Digite o {i + 1}º número: "))
                        break  # Exit the loop if a valid float is entered
                    except ValueError:
                        print("Digite um número válido.")
                soma += n
                l.append(n)
            media = soma / q
            for j in l:
                vari += (j - media) ** 2
            variancia = vari / q
            desvio = math.sqrt(variancia)
            print("A média dos números digitados é  %.2f:" %media)
            print("A variância dos números digitados é: %.2f" %variancia)
            print("O desvio-padrão é %.2f" % desvio)
            inicia = input("Deseja continuar ? (S/N):").upper()
