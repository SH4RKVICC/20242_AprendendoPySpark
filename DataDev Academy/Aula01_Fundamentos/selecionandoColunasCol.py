# Esse métodos são melhores para realizar funções

df.select(col('Selecao'), col('Altura')).show(2) #Utilizando Col

df.select(df['Selecao']).show(2)

# Selecionar Colunas com ALIAS

df.select('Selecao'.alias('Time')).show(2) # Ira dar erro


df.select(df['Selecao'].alias('Time')).show(2) #Criando 'apelido' para coluna selecao com df

df.select(col('Selecao'.alias('Time'))).show(2) # Criando 'apelido para coluna selecao com col'

# Curiosidade;
df.select('Selecao Nome_FIFA Altura'.split()).show(3)



