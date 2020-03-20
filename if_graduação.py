user = str(input("Qual seu tipo de graduação (Tecnologo ou Bacharelado)")).upper().strip()
if user != "Tecnologo" and user != "Bacharelado":
    print("Informe o tipo de graduação!")
elif user == "Bacharelado":
    print("4 até 6 anos")
else:
    print("2 até 3 anos")
