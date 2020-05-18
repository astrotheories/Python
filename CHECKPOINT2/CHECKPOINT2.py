from funcoes import*
x = { "Julia":["julialee@gmail.com", "B@nanaSplit"], "Lucas":["luska.csgo@hotmail.com", "S0uFod4"], "Fernanda":["fernanda-silva@hotmail.com", "Mengao123"], "Joao":["jpedro@hotmail.com", "Lolo55"], "Henrique":["henrique.o@hotmail.com", "belinha123"] }

print("""

██    ██  █████  ███████  █████  ███    ███ ███████ ███    ██ ████████  ██████  ███████ 
██    ██ ██   ██    ███  ██   ██ ████  ████ ██      ████   ██    ██    ██    ██ ██      
██    ██ ███████   ███   ███████ ██ ████ ██ █████   ██ ██  ██    ██    ██    ██ ███████ 
 ██  ██  ██   ██  ███    ██   ██ ██  ██  ██ ██      ██  ██ ██    ██    ██    ██      ██ 
  ████   ██   ██ ███████ ██   ██ ██      ██ ███████ ██   ████    ██     ██████  ███████ 
                                                                                        
                                                          
""")
while True:
    print("""
1 - CADASTRAR
2 - BUSCAR
3 - ALTERAR
4 - EXIBIR
5 - EXCLUIR
6 - SAIR
""")

    num = int(input("\nQual opção você deseja? De 1 a 6\n "))
    if num == 1:
        cadastrar(x)
    elif num == 2:
        buscar(x)
    elif num == 3:
        alterar(x)
    elif num == 4:
        exibir(x)
    elif num == 5:
        excluir(x)
    elif num == 6:
        break
    else:
        print("Favor escolher uma opção de 1 a 6 ")