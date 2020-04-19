user = str(input("Qual seu tipo de graduação (Tecnologo ou Bacharelado)\n")).upper().strip().title()
if user == "Bacharelado":
    print("4 até 6 anos")
elif user == "Tecnologo":
    print("2 até 3 anos")
else:
    print("Graduação inválida")
