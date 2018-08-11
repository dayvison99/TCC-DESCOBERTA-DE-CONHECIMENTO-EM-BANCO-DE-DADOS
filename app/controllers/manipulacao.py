import sqlite3
# Função Delete (excluindo um usuario da tabela)
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

id_Usuario = 1

# funcao responsavel por cadastrar no banco de dados
def inserirUsuarios():
    adastroform = CadastroUsuarioForm()
    if request.method == 'POST' and cadastroform.validate():
        user = User(cadastroform.nome.data,cadastroform.cpf.data,cadastroform.email.data,cadastroform.celular.data,
        cadastroform.nomeUsuario.data,cadastroform.tipo.data,cadastroform.senha.data)
        #,cadastroform.confirm.data)
        db.session.add(user)
        db.session.commit()
        flash('Usuário Cadastro com Sucesso !')
        return redirect(url_for('listagemUsuario'))
    return render_template('cadastroUsuarios.html',
                            cadastroform = cadastroform)




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
