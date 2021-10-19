import sqlite3

conexao = sqlite3.connect('dasededados.db')
cursor = conexao.cursor()

# cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
#                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#                'nome TEXT,'
#                'peso REAL'
#                ')')
#
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Juliana', 65))
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)', {'nome': 'Olivia', 'peso': 10})
# cursor.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)', {'id': None, 'nome': 'Olivia', 'peso': 10})
#
# conexao.commit()


# alterando
# cursor.execute('UPDATE clientes SET nome=:nome WHERE id=:id', {'nome': 'Marcelo', 'id': 2})
# cursor.execute('UPDATE clientes SET nome=:nome WHERE id=:id', {'nome': 'Breno', 'id': 5})
# conexao.commit()

# Deletando
cursor.execute('DELETE FROM clientes WHERE id=:id', {'id':  5})

cursor.execute('SELECT * FROM clientes')
for linha in cursor.fetchall():
    identificador , nome, peso = linha

    print(identificador, nome, peso)


cursor.execute('SELECT nome, peso FROM clientes WHERE peso > 70')
for linha in cursor.fetchall():
    nome, peso = linha
    print(nome, peso)
cursor.close()
conexao.close()