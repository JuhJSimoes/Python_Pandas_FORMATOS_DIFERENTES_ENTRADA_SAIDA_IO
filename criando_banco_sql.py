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
print(engine.table_names())

#Nomes dos alunos da proxima turma

matriculas = pd.read_csv('matriculas.csv', sep=',')
print(matriculas.head(3))

