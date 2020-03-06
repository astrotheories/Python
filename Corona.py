nome = input("Qual o nome: ")
idade = int(input("Qual a idade: "))
risco = input("Eh grupo de risco? (sim ou nao)").upper()
if risco != "SIM" and risco != "NAO":
    risco = input("Entre somente sim ou nao").upper()

if idade < 15 or idade > 60:
    print("Corona!!")
elif risco == "SIM":
    print("Ai minha asma!!")
else:
    print("partiu praia!!")
