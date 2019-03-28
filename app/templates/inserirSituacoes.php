{% extends 'base.html' %}

{% block content%}

<div class="jumbotron"><center>
  <fieldset class="fieldset-border">
    <legend class="legend-border"><h3> Inserção de Situações </h3></legend>
  <br/>
  <br/>
<form action="" method="POST">
<!-- DADOS DAS SITUAÇOES DAS DISCIPLINAS-->
<fieldset>
 <table cellspacing="10">
   <tr>
    <td>
     <label for="periodo">Período :   </label>
    </td>
     <td align="left">
     <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
                    <select name="periodo" class="select" id="periodo" input type="submit"  onclick="chamar1()">
                        <option value="nenhum" disabled selected>-----</option>
                        {%for periodo in periodo  %}
                        <option value={{ periodo.id }}>{{ periodo.nome }}</a></option>

                        {% endfor %}
                    </select>
                </td>
          </tr>
          </tr>
              <tr>
              <td>
                    <label for="status">Disciplina :   </label>
                </td>
                    <td align="left">
                      <script languagem="javascript" >
                      function chamar1(){
                         var a = document.getElementById(periodo.id).value;
                              alert([a]);
                      }</script>

                            <select name="disciplina" class="one input" style="display: none" id ="periodo.id">
                                {%for disciplina in disciplina   %}
                                  <option value={{ disciplina.nome }} >{{ disciplina.nome }}</option>
                                {% endfor %}
                            </select>
                          <!--  <select name="disciplina" class="one input" style="display: none" id="2">
                                {%for disciplina in disciplina   %}
                                  <option value={{ disciplina.nome }}>{{ disciplina.nome }}</option>
                                {% endfor %}
                            </select>
                            <select name="disciplina" class="one input" style="display: none" id="3">
                                {%for disciplina in disciplina   %}
                                  <option value={{ disciplina.nome }}>{{ disciplina.nome }}</option>
                                {% endfor %}
                            </select>
                            <select name="disciplina" class="one input" style="display: none" id="4">
                                {%for disciplina in disciplina   %}
                                  <option value={{ disciplina.nome }}>{{ disciplina.nome }}</option>
                                {% endfor %}
                            </select>
                            <select name="disciplina" class="one input" style="display: none" id="5">
                                {%for disciplina in disciplina   %}
                                  <option value={{ disciplina.nome }}>{{ disciplina.nome }}</option>
                                {% endfor %}
                            </select>
                            <select name="disciplina" class="one input" style="display: none" id="6">
                                {%for disciplina in disciplina   %}
                                  <option value={{ disciplina.nome }}>{{ disciplina.nome }}</option>
                                {% endfor %}
                            </select>-->
           <tr>
                <td>
                    <label for="status">Status :   </label>
                </td>
                <td align="left">
                    <select name="status"  onchange="chamar()" id="status">
                              <option value="nenhum" disabled selected>-----</option>
                              <option value="APROVADO">Aprovado</option>
                              <option value="REPROVADO">Repovado</option>
                              <option value="MATRICULADO">Matriculado</option>
                              <option value="CANCELADO">Desistente</option>
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
  <script languagem="javascript" >
    function chamar(){
     var valor = document.getElementById("periodo").value;
     var disci = document.getElementById(periodo.id).value;
     var status = document.getElementById("status").value;
          alert([valor,disci,status]);
      }
    </script>
   </td>
  </tr>
 </table>
</fieldset>
<br />
<a href='/analise'><button  title="Inserir! " class="btn btn-info btn-lg" type="button">Finalizar</button></a>
<a href='/listagem/{{ disciplina.nome }}'><button  title="Inserir! " class="btn btn-info btn-lg" type="submit">INSERIR</button></a>
</form>
</center></div>
{% endblock %}
