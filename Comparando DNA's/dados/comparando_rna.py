import matplotlib.pyplot as plt
import os

# Abrindo os arquivos da bactéria
dir_path = os.path.dirname(os.path.realpath(__file__))
enter = open(dir_path + '/bacteria.fasta').read()
output = open('bacteria.html', 'w')

# Criação de dicionário para os pares de RNA
counter = {}

# Inserindo no dicionário os pares possíveis que podem existir
for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        counter[i+j] = 0

# Retirando as quebras de linhas do arquivo
enter = enter.replace("\n", '')

# Analisando o RNA da bactéria para ver se existem os pares
for k in range(len(enter)-1):
    # Inserindo as duas letras no dicionário criado
    counter[enter[k] + enter[k+1]] += 1


# Criando um HTML para visualização

# Contador
i = 1

for k in counter:
    transparence = counter[k]/max(counter.values())
    output.write("<div style ='width:100px; border:1px solid #111; height:100px; float:left;color:#fff; background-color:rgba(0,0,255, "+str(transparence)+"')>"+k+"</div>")

    if i % 4 == 0:
        output.write("<div style='clear:both'></div>")
    
    i += 1


output.close()