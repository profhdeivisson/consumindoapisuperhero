import urllib.request
from json import loads
from math import ceil

url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
webpage = urllib.request.urlopen(url).read().decode()
js = loads(webpage)
print(f'Existem {len(js)} personagens')

def listar_biografia(person):
    print(f'|Personagem: {person["name"]}|')
    print('-'*90)
    print(f'|   Biografia---------')
    print(f'|    Nome Completo:', person['biography']['fullName'])
    print(f'|    Apelido(s):', ', '.join(person['biography']['aliases']))
    print('-'*90)
    print(f'|   Estatística de Potência:')

def listar_poderes(lista):
    for chave in lista:
        barra = "▒"
        valores = ceil(lista.get(chave) // 2) + 1
        print(f'|    {chave:>12}: {valores:^5}{barra*valores:12}')

def mostrar_todos():
    for personagem in js:
        listar_biografia(personagem)
        listar_poderes(personagem['powerstats'])
        print('-'*90)

def mostrar_n_personagens():
    quantidade = int(input('Quantos heróis deseja ver?'))
    for qtd in range(quantidade):
        listar_biografia(js[qtd])
        listar_poderes(js[qtd]['powerstats'])
        print('-'*90)

def pesquisar():
    pesquisa_personagem = input('Digite o nome do personagem:')
    for personagem in js:
        if pesquisa_personagem.lower() not in personagem.get('name').lower():
            continue
        elif pesquisa_personagem.lower() in personagem.get('name').lower():
            listar_biografia(personagem)
            listar_poderes(personagem['powerstats'])
            print('-'*90)

while True:
    numero = input('''
    [1] = Mostrar todos os personagens
    [2] = Pesquisar Personagem
    [3] = Mostrar um número [X] de Personagens
    [4] = Sair
    Digite um valor para prosseguir:''')
    if not numero.isnumeric():
        print("Digite apenas números!")
    else:
        numero = int(numero)
        if numero in range(1, 5):
            if numero == 1:
                mostrar_todos()
            if numero == 2:
                pesquisar()
            if numero == 3:
                mostrar_n_personagens()
            if numero == 4:
                print('Saindo...')
                break
        else:
            print("Valor digitado, inválido!")