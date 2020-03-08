genero = input('''Selecione o seu genero:
1)FEMININO
2)MASCULINO
Selecione seu genero: ''')

per = input('''Entrar como:
1)ADM
2)USR
3)GUEST

Entrar como? :''')

if genero == '1' and per == '1':
	print('Ola Administradora')

elif genero == '2' and per == '1':
	print('Ola Administrador')

elif genero == '1' and per == '2':
	print('Ola Usuaria')

elif genero == '2' and per == '2':
	print('Ola Usuario')

elif genero == '1' and per == '3':
	print('Ola Visitante')

elif genero == '2' and per == '3':
	print('Ola Visitante')

else:
	print('Ola Desconhecido')
