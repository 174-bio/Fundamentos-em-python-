#4. Receba nome, peso e altura. Calcule IMC.
# Entrada
nome=str(input("Digite seu nome: "))
peso=int(input("digite seu peso: "))
altura= float(input("Digite sua altura: "))

print(f"{nome} seu peso é {peso} e seu imc é {peso/(altura*altura):.2f}")