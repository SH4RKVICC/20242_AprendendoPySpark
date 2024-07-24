# Verificar Tipos de Colunas

df.printSchema()

# Verificando dados nulos

df.toPandas().isna().sum() #Transformando em Pandas, verificar valores nulos e somando

# Obs: só fazer toPanda em arquivos pequenos