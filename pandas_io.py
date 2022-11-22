import pandas as pd
import numpy as np
import html5lib

#Criando os nomes 

nomes_f = pd.read_json('https://guilhermeonrails.github.io/nomes_ibge/nomes-f.json')
nomes_m = pd.read_json('https://guilhermeonrails.github.io/nomes_ibge/nomes-m.json')
print(nomes_f, nomes_m, '\n')

print(nomes_f.sample(5), '\n')
print(nomes_m.sample(5), '\n')

print('Quantidade de nomes: ' + str(len(nomes_f) + len(nomes_m)), '\n')

frames = [nomes_f, nomes_m]
nomes = pd.concat(frames)['nome'].to_frame()
print(nomes.sample(5), '\n')


#Incluindo ID dos alunos
np.random.seed(123)
total_alunos = len(nomes)
print(total_alunos, '\n')

nomes['id_aluno'] = np.random.permutation(total_alunos) + 1
print(nomes.sample(15), '\n')

dominios = ['@dominioemail.com.br', '@servicodoemail.com']
nomes['dominio'] = np.random.choice(dominios, total_alunos)
nomes['email'] = nomes.nome.str.cat(nomes.dominio).str.lower()
print(nomes.sample(5), '\n')

#Criando a tabela de cursos
url = 'http://tabela-cursos.herokuapp.com/index.html'
cursos = pd.read_html(url)
print(type(cursos), '\n')
cursos = cursos[0] #transformou a lista em dataframe
print(type(cursos), '\n')
print(cursos.head(), '\n')

