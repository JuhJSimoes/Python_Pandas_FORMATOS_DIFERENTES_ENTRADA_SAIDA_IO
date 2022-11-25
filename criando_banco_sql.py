from sqlalchemy import create_engine, MetaData, Table, inspect
import pandas as pd

engine = create_engine('sqlite:///:memory:')
#print(type(engine))

matriculas_por_curso = pd.read_csv('matriculas_por_curso.csv', sep=',')
print(matriculas_por_curso.head(3))


matriculas_por_curso.to_sql('matriculas', engine)
inspector = inspect(engine)
print(inspector.get_table_names(), '\n')

#Buscando do banco sql

query = 'select * from matriculas where quantidade_de_alunos < 20'
print(pd.read_sql(query, engine),'\n')

muitas_matriculas = pd.read_sql_table('matriculas', engine, columns=['nome_do_curso', 'quantidade_de_alunos'])
print(muitas_matriculas, '\n')

muitas_matriculas = muitas_matriculas.query('quantidade_de_alunos > 70')
print(muitas_matriculas, '\n')

#Escrevendo no banco

muitas_matriculas.to_sql('muitas_matriculas', con = engine)
inspector = inspect(engine)
print(inspector.get_table_names(), '\n')

#Nomes dos alunos da proxima turma

matriculas = pd.read_csv('matriculas.csv', sep=',')
print(matriculas.head(3), '\n')

id_curso = 15
proxima_turma = matriculas.query('id_curso == {}'.format(id_curso))

nomes = pd.read_csv('alunos.csv', sep=',')
cursos = pd.read_csv('cursos.csv', sep=',')
#proxima_turma = proxima_turma.set_index('id_aluno').join(nomes.set_index('id_aluno'))
#print(proxima_turma, '\n')
print(nomes.columns.to_list())
#proxima_turma = proxima_turma.set_index('id_aluno').join(nomes.set_index('id_aluno'))['nome']
#print(proxima_turma, '\n')
proxima_turma = proxima_turma.set_index('id_aluno').join(nomes.set_index('id_aluno'))['nome'].to_frame()

nome_curso = cursos.loc[id_curso]
print(nome_curso, '\n')
nome_curso = nome_curso['nome_do_curso']
print(nome_curso, '\n')

proxima_turma = proxima_turma.rename(columns={'nome': 'Aluno do curso de {}'.format(nome_curso)})
print(proxima_turma)

proxima_turma.to_excel('proxima_turma.xlsx', index = False)