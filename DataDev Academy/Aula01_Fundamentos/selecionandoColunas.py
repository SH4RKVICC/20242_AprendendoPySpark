# Selecionar Colunas

df.select('Selecao').show(5) #Selecionando uma coluna

df.select('Selecao', 'Nome_FIFA').show(5) #Selecionando duas colunas

df.select('Selecao', 'nome_fifa').show(5) #Selecionando coluna com nome em caixa baixa (note que não atrapalha a consulta)

df.select('Selecao', 'NOME_FIFA').show(5)