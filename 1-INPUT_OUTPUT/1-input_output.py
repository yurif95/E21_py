from time import sleep


nome=str(input('Qual seu nome: '))
idade=int(input('Qual sua idade: '))
cidade=str(input('Qual cidade você mora: '))
print('Analisando...')
sleep(2)

print(f"Nome: {nome}\nIdade: {idade}\nCidade: {cidade} ")



# Exemplo de cálculo simples com a idade

idade_futura=idade+5
print(f'Em 5 anos você tera {idade_futura} anos ')

# Mensagem Personalizada

print(f'Olá {nome} é um prazer em te conhecer!\nQue legal que você mora na cidade {cidade}!') 