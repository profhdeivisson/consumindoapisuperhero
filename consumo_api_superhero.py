import urllib.request, json, math

url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
webpage = urllib.request.urlopen(url).read().decode()
js = json.loads(webpage)
print(f'Existem {len(js)} personagens')

def mostrar_todos():
    for personagem in js:
        print(f'|Personagem: {personagem["name"]}|')
        print('-'*90)
        print(f'|   Biografia:')
        print(f'|    Nome Completo:', personagem['biography']['fullName'])
        print(f'|    Apelido(s):', ', '.join(personagem['biography']['aliases']))
        print('-'*90)
        print(f'|   Estatística de Potência:')
        
        for power in personagem['powerstats']:
            barra = "▒"
            valores = math.ceil(personagem['powerstats'][power] // 2) + 1
            print(f'|    {power:>12}: {valores:^5}{barra*valores:12}')
        print('-'*90)

def mostrar_n_personagens():
    quantidade = int(input('Quantos heróis deseja ver?'))
    for qtd in range(quantidade):
        print(f'|Personagem: {js[qtd].get("name")}|')
        print('-'*90)
        print(f'|   Biografia:')
        print(f'|    Nome Completo:', js[qtd]['biography']['fullName'])
        print(f'|    Apelido(s):', ', '.join(js[qtd]['biography']['aliases']))
        print('-'*90)
        print(f'|   Estatística de Potência:')
        
        for power in js[qtd]['powerstats']:
            barra = "▒"
            valores = math.ceil(js[qtd]['powerstats'][power] // 2) + 1
            print(f'|    {power:>12}: {valores:^5}{barra*valores:12}')
        print('-'*90)

def pesquisar():
    pesquisa_personagem = input('Digite o nome do personagem:')
    for personagem in js:
        if pesquisa_personagem.lower() not in personagem.get('name').lower():
            continue
        elif pesquisa_personagem.lower() in personagem.get('name').lower():
            print(f'|Personagem: {personagem["name"]}|')
            print('-'*90)
            print(f'|   Biografia:')
            print(f'|    Nome Completo:', personagem['biography']['fullName'])
            print(f'|    Apelido(s):', ', '.join(personagem['biography']['aliases']))
            print('-'*90)
            print(f'|   Estatística de Potência:')
            
            for power in personagem['powerstats']:
                barra = "▒"
                valores = math.ceil(personagem['powerstats'][power] // 2) + 1
                print(f'|    {power:>12}: {valores:^5}{barra*valores:12}')
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
        if numero == str(1) or numero == str(2) or numero == str(3) or numero == str(4):
            if numero == str(1):
                mostrar_todos()
            elif numero == str(2):
                pesquisar()
            elif numero == str(3):
                mostrar_n_personagens()
            else:
                print("Saindo...")
                break
        else:
            print("Valor digitado, inválido!")