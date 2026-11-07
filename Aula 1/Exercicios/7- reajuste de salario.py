# 7. Receba nome, cargo e salário e acrescente 10%.
nome=str(input("qual seu nome?: "))
cargo= str(input("qual seu cargo: "))
sal= float(input('qual seu salario: '))

print(f"Seu nome é {nome} seu cargo é {cargo} e seu salario com um aumento de 10% é R${sal*1.1:.2f} ")