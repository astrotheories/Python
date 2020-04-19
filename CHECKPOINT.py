import re

print('''                                                                 
██████╗  █████╗ ███╗   ██╗██████╗  █████╗ ███████╗    ██╗██████╗  █████╗ ██████╗  █████╗ ███████╗
██╔══██╗██╔══██╗████╗  ██║██╔══██╗██╔══██╗██╔════╝    ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝
██████╔╝███████║██╔██╗ ██║██║  ██║███████║███████╗    ██║██████╔╝███████║██║  ██║███████║███████╗
██╔══██╗██╔══██║██║╚██╗██║██║  ██║██╔══██║╚════██║    ██║██╔══██╗██╔══██║██║  ██║██╔══██║╚════██║
██████╔╝██║  ██║██║ ╚████║██████╔╝██║  ██║███████║    ██║██║  ██║██║  ██║██████╔╝██║  ██║███████║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝
                                                                 
''')

lista_um = ["QUEEN", "ROLLING STONES", "THE SMITHS", "THE BEATLES", "AC/DC", "ARCTIC MONKEYS", "DAY6", "FALL OUT BOY", "PANIC! AT THE DISCO", "GREEN DAY", "GROUPLOVE", "LINKIN PARK", "MAROON FIVE", "MY CHEMICAL ROMANCE", "ONE DIRECTION", "THE ROSE", "THE STROKES", "TWENTY ONE PILOTS", "NIRVANA", "THE KILLERS", "A-HA", "COLDPLAY", "RADIOHEAD", "BON JOVI", "THE DOORS", "PEARL JAM", "THE CURE", "THE POLICE", "TAME IMPALA", "AEROSMITH", "THE RUNAWAYS", "NIRVANA", "ABBA", "THE KOOKS", "OASIS", "THE NEIGHBOURHOOD", "THE 1975", "THE KILLERS", "PINK FLOYD", "CAPITAL INICIAL", "LEGIÃO URBANA", "RAMONES", "IRON MAIDEN", "METALLICA", "FOO FIGHTERS", "ROUPA NOVA", "GUNS N' ROSES", "PARALAMAS DO SUCESSO", "RAIMUNDOS", "BLACK SABBATH", "LYNYRD SKYNYRD", "LIMP BIZKIT", "NICKELBACK", "BACKSTREET BOYS"]

while True:
      interacao = input("Qual banda deseja consultar?\n").upper()
      compilado = re.compile(r"[A-Z0-9!/ ']*"+interacao+r"[A-Z0-9!/ ']*")
      lista_dois = filter(compilado.match, lista_um)
      lista_dois = (list(lista_dois))
      if lista_dois == []:
            print("Banda não encontrada.")
      else:
            bandas = "BANDAS"
            print("+---------------------------------------------+")
            print(f"| {bandas: ^43} |")
            print("+---------------------------------------------+")
            cont = 0
            for p in lista_dois:
                  cont += 1
                  print(f"| {cont: <3} = {p: <37} |")
                  print("+---------------------------------------------+")
      continuar = input("Deseja consultar novamente ?? Y ou N:\n").upper().strip()
      while continuar != "Y" and continuar != "N":
            continuar = input("Digite apenas Y ou N ??:\n").upper().strip()
      if continuar == "Y":
            continue
      else:
            break