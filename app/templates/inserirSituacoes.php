{% extends 'base.html' %}

{% block content%}

<div class="jumbotron"><center>

  <fieldset class="fieldset-border">
    <legend class="legend-border"><h3> Inserção de Situações </h3></legend>
  <br/>
  <br/>
<form action="" method="GET">
<!-- DADOS DAS SITUAÇOES DAS DISCIPLINAS-->
<fieldset>
 <table cellspacing="10">
   <tr>
    <td>
     <label for="periodo">Período : - </label>
    </td>
     <td align="left">
     <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
  <select name='periodo' class="select">
         <option value="nenhum">-----</option>
         <option value="1">1º Período</option>
         <option value="2">2º Período</option>
         <option value="3">3º Período</option>
         <option value="4">4º Período</option>
         <option value="5">5º Período</option>
         <option value="6">6º Período</option>
      </select>
    </td>
   </tr>
 </tr>
  <tr>
       <td>
      <label for="disciplina">Disciplinas : -</label>
       </td>
       <td align="left">
                <select name="disciplina" class="one input" style="display: none" id="1">
                  <option value="">-----</option>
                  <option value="Algoritmo">Algoritmo</option>
                  <option value="Fundamentos_Computacao">Fundamentos da Computação</option>
                  <option value="Ingles">Inglês Técnico</option>
                  <option value="Logica_Matematica">Lógica Matematica</option>
                  <option value="Matematica_Computacional">Matemática Computacional</option>
                  <option value="Lingua_Portuguesa">Língua Portuguesa</option>
                  <option value="TGA">Teoria Geral da Administração</option>
                </select>
                <select name="disciplina" class="one input" style="display: none" id="2">
                      <option value="">-----</option>
                      <option value="Arquitetura_Organizacao">Arquitetura e Organização</option>
                      <option value="Banco_Dados_I">Banco_Dados_I</option>
                      <option value="Fundamentos_Sistemas_Informacao">Fundamentos de Sistemas Informação</option>
                      <option value="Modelos_Paradigmas_Programacao">Modelos e Paradigmas de Programação</option>
                      <option value="Programacao_Estruturada">Programação Estruturada</option>
                      <option value="Sistemas_Operacionais">Sistemas Operacionais</option>
                    </select>
                    <select name="disciplina" class="one input" style="display: none" id="3">
                          <option value="">-----</option>
                          <option value="Banco_Dados_II">Banco de DadosII</option>
                          <option value="Estatisticas">Estatisticas</option>
                          <option value="Programacao_Orientada_Objeto">Programação Orientada a Objeto</option>
                          <option value="Programacao_Web_I">Programação WebI</option>
                          <option value="Redes_Computadores_I">Redes de ComputadoresI</option>
                      </select>
                      <select name="disciplina" class="one input" style="display: none" id="4">
                            <option value="">-----</option>
                            <option value="Analise_Projeto_Sistema">Analíse e Projeto de Sistema</option>
                            <option value="Engenharia_Software">Engenharia de Software</option>
                            <option value="Programacao_Web_II">Programacao WebII</option>
                            <option value="Programacao_Sistemas_Corporativos">Programação de Sistemas Corporativos</option>
                            <option value="Redes_Computadores_II">Redes de ComputadoresII</option>
                      </select>
                      <select name="disciplina" class="one input" style="display: none" id="5">
                            <option value="">-----</option>
                            <option value="Arquitetura_Software">Arquitetura de Software</option>
                            <option value="Auditoria_Seguranca">Auditoria e Segurança</option>
                            <option value="Empreendedorismo">Empreendedorismo</option>
                            <option value="Gerencia_projetos">Gerencia de Projetos</option>
                            <option value="Interface_Homem_Maquina">Interface Homem Maquina</option>
                            <option value="Contabilidade">Introdução a Contabilidade</option>
                            <option value="Processo_Unificado">Processo Unificado D S</option>
                      </select>
                      <select name="disciplina" class="one input" style="display: none" id="6">
                            <option value="">-----</option>
                            <option value="Gerencia_Recursos_Informacional">Gerência de Recursos Informacional</option>
                            <option value="Legislacao_Aplicada">Legislação Aplicada</option>
                            <option value="Metodologias_Ageis">Metodologias Ágeis</option>
                            <option value="Metodologia_Cientifica">Metodologia Cientifica</option>
                            <option value="Qualidade_de_Software">Qualidade de Software</option>
                            <option value="Seminarios">Seminários</option>
                            <option value="Topicos_Especiais">Tópicos Especiais</option>
                      </select>
               </td>
           </tr>
           <tr>
                <td>
                    <label for="status">Status : - </label>
                </td>
                <td align="left">
                    <select name="status">
                              <option value="nenhum">-----</option>
                              <option value="aprovado">Aprovado</option>
                              <option value="reprovado">Repovado</option>
                              <option value="matriculado">Matriculado</option>
                              <option value="cancelado">Desistente</option>
                    </select>
               </td>
    <script type="text/javascript">
    $('.select').on({change: listChildren}).trigger('change');

function listChildren(){

if ( $(this).val() != '' ) {
children = $('option').val();
$(".input").hide();
$("#" + $(this).val() ).show();
}

}
    </script>

   </td>

  </tr>
 </table>
</fieldset>
<br />
<!--<a href="{{ url_for('situacoes') }}">-->
<button title="Inserir! " class="btn btn-primary" type="submit">INSERIR</button>

</form>
</center></div>
{% endblock %}
