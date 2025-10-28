#write files with open fucntion
with open ('dados.txt','w') as f:
    f.write('olá tudo bem?')

#read files  with open function
with open('dados.txt', 'r') as f:
    conteudo = f.read()
print(conteudo)