priE = int(input("Qual a chave privada de Evan?"))
priC = int(input("Qual a chave privada de Connor?"))

J = int(input("Qual o valor de J?"))
Z = int(input("Qual o valor de Z?"))

pubE = (Z**priE)
pubE = pubE%J

pubC = (Z**priC)
pubC = pubC%J

compE = (pubC**priE)
compE = compE%J

compC = (pubE**priC)
compC = compC%J

print("A chave partilhada de Evan é: "+ str(compE))
print("A chave partilhada de Connor é: "+ str(compC))