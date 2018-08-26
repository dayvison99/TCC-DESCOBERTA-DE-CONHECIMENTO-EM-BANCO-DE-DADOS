{% extends 'base.html' %}

{% block content%}
<div class="jumbotron"><center>
  <fieldset class="fieldset-border">
    <legend class="legend-border"><h3> Inserção de Situações </h3></legend>
  <br/>
  <br/>
<form action="" method="post">
<!-- DADOS DAS SITUAÇOES DAS DISCIPLINAS-->
<fieldset>
 <table cellspacing="10">
   <tr>
    <td>
     <label for="periodo">Período : - </label>
    </td>
    <td align="left">
     <select name="periodo" id="periodo" onclick="chamar()">
     <option value="">-----</option>
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
     <label for="disciplina">Disciplina : -</label>
    </td>
    <td align="left">
     <select name="disciplina">
      <option value="">-----</option>
     <option value="algoritmo">Algoritmo</option>
     <option value="logicaMatematica">Lógica Matematica</option>
     <option value="matematicaComputacional">Matemática Computacional</option>
     <option value="linguaPortuguesa">Língua Portuguesa</option>
     <option value="fundamentosdaComputacao">Fundamentos da Computação</option>
     <option value="inglesTecnico">Inglês Técnico</option>
     <option value="teoriaGeraldaAdministracao">Teoria Geral da Administração</option>
     </select>
    </td>
   </tr>
   <tr>
    <td>
     <label for="status">Status : - </label>
    </td>
    <td align="left">
    <select name="satatus">
    <option value="nenhum">-----</option>
    <option value="aprovado">Aprovado</option>
    <option value="reprovado">Repovado</option>
    <option value="matriculado">Matriculado</option>
    <option value="cancelado">Cancelado</option>
    </select>
   </td>
  </tr>
 </table>
</fieldset>
<br />
<a href="{{ url_for('situacoes') }}"><button title="Inserir! " class="btn btn-primary" type="button">INSERIR</button> </a>

</form>
</center></div>
{% endblock %}
