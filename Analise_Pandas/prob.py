
# coding: utf-8

# # SASA - SISTEMA DE ANALISE DE SISTUAÇÕES ACADEMICA

# In[1]:


import pandas as pd
import numpy as np


# ### Lendo os dados

# In[2]:


dados = pd.read_csv('dateset.csv')


# In[22]:


date = pd.DataFrame(dados)


# In[23]:


date


# In[5]:


dados[(dados['disciplina']=='') &  (dados['situacaoDisciplina']=='APROVADO')]


# ##### Contando Cada Situação Possivel (APROVADO e REPROVADO)

# In[6]:


total=dados['situacaoDisciplina'].count()


# In[7]:


aprovado = dados[dados.situacaoDisciplina=='APROVADO'].count()


# In[8]:


reprovado = dados[dados.situacaoDisciplina=='REPROVADO'].count()


# #### Probabilidade para cada disciplina

# In[41]:


def resultados(disciplinas): #disciplina,situacaoDisciplina
    #print(disciplinas)
    a = []
        #for i in range(1):
        #    probabilidadeTotal = dados.loc[(dados['disciplina']==disciplina)].count()
        #    probabilidade = dados.loc[(dados['disciplina']==disciplina) & (dados['situacaoDisciplina']==situacaoDisciplina)].count()
        #    a = probabilidade/probabilidadeTotal
       
        #    return "A probabilidaded  aluno ser ",situacaoDisciplina,'em', disciplina, a[i],'%'
        
    for d in disciplinas:
        #print(d)
        probabilidadeTotal = dados.loc[(dados['disciplina']==d[0])].count()
        print(probabilidadeTotal)
        probabilidade = dados.loc[(dados['disciplina']==d[0]) & (dados['situacaoDisciplina']==d[1])].count()
        a.append([d[0], d[1], probabilidade/probabilidadeTotal])
    
    msg = """A probabilidade do aluno obter um determinado resultado para as seguintes disciplinas:bi
             |          Disciplina         |    Resultado   |    Probabilidade    |"""
    for i in a:
        #print(i)
        msg+= '{0} | {1} | {2}%'.format(i[0], i[1], i[2])

    return msg


# In[42]:


print(resultados([('Algoritmo','REPROVADO'), ('TGA','APROVADO')]))


# In[27]:


#resultados('TGA','APROVADO')

