def cadastrar(x):
    var = "Sim"
    while var == "Sim":
        nome = input("\nQual nome deseja cadastrar? ").title()
        x[nome] = [input("E-mail: "), input("Senha: ")]
        print("E-mail cadastrado com sucesso!")
        var = input("Deseja cadastrar um novo E-mail? (Sim ou Nao) ").title()

def buscar(x):
    nome = input("\nQual nome deseja buscar? ").title()
    if x.get(nome) != None:
        lista = x.get(nome)
        print("E-mail: ", lista[0])
        print("Senha: ", lista[1])

def alterar(x):
    nome = input("\nQual nome deseja alterar? ").title()
    if x.get(nome) != None:
        x[nome] = [input("E-mail: "), input("Senha: ")]
    else:
        print("Não existe")

def exibir(x):
    for a, lista in x.items():
        print("\nNome:   ", a)
        print("E-mail: ", lista[0])
        print("Senha:  ", lista[1])

def excluir(x):
    nome = input("\nQual nome deseja excluir? ").title()
    if x.get(nome) != None:
        del x[nome]
    else:
        print("Nome não encontrado")