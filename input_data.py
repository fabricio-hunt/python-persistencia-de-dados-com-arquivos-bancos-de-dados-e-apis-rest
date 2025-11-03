#Funções para entrada de dados do usuário

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

with open('input_data.txt', 'a') as f:
    f.write(f'Nome: {nome}\n')
    f.write(f'Idade: {idade}\n')

