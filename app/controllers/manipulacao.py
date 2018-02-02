import sqlite3
# Função Delete (excluindo um usuario da tabela)
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

id_Usuario = 1


cursor.execute("""
DELETE FROM clientes
WHERE id = ?
""", (id_cliente,))

conn.commit()

print('Usuario excluido com sucesso.')

conn.close()
