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
            </tr>
              <tr>
              <td><h3>
                    <label for="status">Disciplina :   </label>
                  <h3>
                </td>
                    <td align="left" ><h4>
                      <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
                      <select name="disciplina"class="select" input type="submit"  id ="disciplina">
                          {%for disciplina in disciplina   %}
                            <option value={{ disciplina.nome }} >{{ disciplina.nome }}</option>
                          {% endfor %}
                   </select>
                    <h4></td>
           <tr>
                <td><h3>
                    <label for="status">Status :   </label>
                </td>
                <td align="left"><h4>
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
    {%for periodo in periodo  %}
  <script languagem="javascript" >
    function chamar(){
     var disci = document.getElementById("disciplina").value;
     var status = document.getElementById("status").value;
          alert([disci,status]);
      }
    </script>
      {% endfor %}
   </td>
  </tr>
 </table>
</fieldset>
<br />
<a href='/analise/'><button  title="Inserir! " class="btn btn-info btn-lg" type="button">ddFinalizar</button></a>

 {%for disciplina in disciplina %}
<a href='/analise/{{ disciplina.nome}}/'><button  title="Inserir! " class="btn btn-info btn-lg" type="button">Finalizar</button></a>

<a href='/listagem/{{ disciplina.nome }}'><button  title="Inserir! " class="btn btn-info btn-lg" type="submit">INSERIR</button></a>
{% endfor %}
</form>
</center></div>
{% endblock %}
