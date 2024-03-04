import sqlite3

BancoDeDados = sqlite3.connect('atividades')
cursor = BancoDeDados.cursor()

# 1. Crie uma tabela chamada "alunos" com os seguintes campos: id(inteiro), nome (texto), idade (inteiro) e curso (texto).
# Criação da tabela "alunos":
cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(200));')

# 2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
# Inserção de registros na tabela "alunos":

cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(1,"Isadora",29,"Biotecnologia")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(2,"João",18,"Engenharia")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(3,"Maria",24,"Medicina")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(4,"Pedro",19,"Filosofia")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(5,"Ana",20,"Oceanografia")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(6,"Carlos",31,"Engenharia")')

# 3. Consultas Básicas - Escreva consultas SQL para realizar as seguintes tarefas:
# a) Selecionar todos os registros da tabela "alunos".
dados = cursor.execute('SELECT * FROM alunos')
for alunos in dados:
    print(alunos)

# b) Selecionar o nome e a idade dos alunos com mais de 20 anos:
dados = cursor.execute('SELECT nome,idade FROM alunos WHERE idade>20')

# c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética:
dados = cursor.execute('SELECT * FROM alunos WHERE curso=Engenharia ORDER BY nome') 

# d) Contar o número total de alunos na tabela:
dados = cursor.execute('SELECT COUNT(*) AS total_alunos FROM alunos') 

# 4. Atualização e Remoção
# a) Atualize a idade de um aluno específico na tabela.
cursor.execute('UPDATE alunos SET idade=17 WHERE nome="Pedro"')

# b) Remova um aluno pelo seu ID:
cursor.execute('DELETE FROM alunos WHERE id=2')

# 5. Criar uma Tabela e Inserir Dados
# Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.
cursor.execute('CREATE TABLE clientes(id INT, nome VARCHAR(100), idade INT, saldo FLOAT);')

cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(1,"Vera",49,460.52)')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(2,"Cássio",20,140.01)')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(3,"Juan",63,824.13)')

# 6. Consultas e Funções Agregadas - Escreva consultas SQL para realizar as seguintes tarefas:
# a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
infos = cursor.execute('SELECT * FROM clientes')
for clientes in infos:
    print(clientes)
infos = cursor.execute('SELECT nome,idade FROM clientes WHERE idade>30')

# b) Calcule o saldo médio dos clientes:
cursor.execute('SELECT AVG(saldo) AS saldo_medio FROM clientes')

# c) Encontre o cliente com o saldo máximo:
cursor.execute('SELECT * FROM clientes ORDER BY saldo DESC LIMIT 1')

# d) Conte quantos clientes têm saldo acima de 1000:
cursor.execute('SELECT COUNT(*) AS clientes_acima_de_1000 FROM clientes WHERE saldo>1000')

# 7. Atualização e Remoção com Condições
# a) Atualize o saldo de um cliente específico.
cursor.execute('UPDATE clientes SET saldo = 2500.00 WHERE nome="Vera"')

# b) Remova um cliente pelo seu ID:
cursor.execute('DELETE FROM clientes WHERE id=3')

# 8. Junção de Tabelas - Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real). Insira algumas compras associadas a clientes existentes na tabela "clientes". 
# Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.
cursor.execute('CREATE TABLE compras(id INT, cliente_id INTEGER, produto VARCHAR(200), valor REAL);')

cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(1,1,Macarrão,8.60)')
cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(1,2,Vinho,45.99)')
cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(1,1,Chocolate,2.53)')

datas = cursor.execute('SELECT * FROM compras')
for compras in datas:
    print(compras)

datas = cursor.execute('SELECT nome,produto,valor FROM compras INNER JOIN clientes ON compras.id=clientes.id'

BancoDeDados.commit()
BancoDeDados.close()