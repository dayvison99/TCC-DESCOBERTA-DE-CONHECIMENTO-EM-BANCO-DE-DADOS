import sqlite3
# Função Delete (excluindo um usuario da tabela)
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

id_Usuario = 1

# funcao responsavel por cadastrar no banco de dados
def inserirUsuarios():
    cursor.execute("""
        INSERT INTO temperature
        (ususarios)
        VALUES (?)
    """, (message,))

    conn.commit()
    conn.close()




def editar_usuarios():
    form = SQLFORM(Usuario, request.args(0, cast=int))
    if form.process().accepted:
        session.flash = 'Filme atualizado: %s' % form.vars.titulo
        redirect(URL('listagemUsuario'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return dict(form=form)


def getUsuarios():
    cursor.execute("""
        SELECT id,nome,cpf,email,nomeUsuario FROM usuario
        ORDER BY nome;
        """)

        return cursor.fetchall()

        conn.close()





cursor.execute("""
DELETE FROM clientes
WHERE id = ?
""", (id_cliente,))

conn.commit()

print('Usuario excluido com sucesso.')

conn.close()
