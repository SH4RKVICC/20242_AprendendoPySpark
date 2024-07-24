# SUBSTRING utiliza caracteres de outras colunas

# Criando abreviatura de selecao
df.withColumn('Sub', substring('Selecao', 1, 3)).show(3)

# Criando Coluna AnoNasc e a Implementando na tabela

df = df.withColumn('AnoNasc', substring('Nascimento', -4, 4))