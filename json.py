import json
dados = {'nome': 'Ana',
         'idade': 32,
         'enderecos': ['endereço A','endereço B']}

with open('dados.json', 'w') as f:
    json.dump(dados, f)