# Adicionando um mesmo dado em todas as colunas
df.withColumn('WorldCup', lit(2018)).show(5) 

# Utilizando duas colunas para gerar um novo valor
df.withColumn('coluna_nova', lit(col('Altura') - col('Peso'))).show(5)