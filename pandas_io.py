import pandas as pd
import numpy as np
import html5lib
import seaborn as sns
import matplotlib.pyplot as plt

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


#Alterando o index de cursos
cursos = cursos.rename(columns={'Nome do curso' : 'nome_do_curso'})
print(cursos.head(5), '\n')

cursos['id'] = cursos.index+1
print(cursos.head(5), '\n')

cursos = cursos.set_index('id')
print(cursos.head(5), '\n')

#Matriculando os alunos nos cursos
print(nomes.sample(5), '\n')

nomes['matriculas'] = np.ceil(np.random.exponential(size = total_alunos) * 1.5).astype(int)
print(nomes.sample(10), '\n')

print(nomes.matriculas.describe())

sns.displot(nomes.matriculas)
#plt.show()

print(nomes.matriculas.value_counts(), '\n')

#Selecionando cursos
todas_matriculas = []
x = np.random.rand(20)
prob = x / sum(x)

for index, row in nomes.iterrows():
    id = row.id_aluno
    matriculas = row.matriculas
    for i in range(matriculas):
        mat = [id, np.random.choice(cursos.index, p = prob)]
        todas_matriculas.append(mat)
        
matriculas = pd.DataFrame(todas_matriculas, columns=['id_aluno', 'id_curso'])
matriculas.to_csv('matriculas.csv', index = False)
print(matriculas.head(),'\n')

print(matriculas.groupby('id_curso').count().join(cursos['nome_do_curso'])
      .rename(columns = {'id_aluno' : 'quantidade_de_alunos'}), '\n')

matriculas_por_curso = matriculas.groupby('id_curso').count().join(cursos['nome_do_curso']).rename(columns = {'id_aluno' : 'quantidade_de_alunos'})
print(matriculas_por_curso, '\n')

#Saida em diferentes formatos

matriculas_por_curso.to_csv('matriculas_por_curso.csv', index = False)
matriculas_json = matriculas_por_curso.to_json()
print(matriculas_json, '\n')

matriculas_html = matriculas_por_curso.to_html()
print(matriculas_html, '\n')

nomes.to_csv('alunos.csv', sep=',', index = False)
cursos.to_csv('cursos.csv', sep=',', index = False)

