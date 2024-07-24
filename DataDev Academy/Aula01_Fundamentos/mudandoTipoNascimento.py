# Separando dia e criando uma coluna
dia = udf(lambda x: x.split('.')[0])
df = df.withColumn('Dia', dia('Nascimento'))

df.show(6)
# Separando Mes e criando uma coluna

mes = udf(lambda x: x.split('.')[1])

df = df.withColumn('Mes', mes('Nascimento'))

df.show(6)

df = df.withColumn('Data_Nascimento', concat_ws('-', 'Dia', 'Mes', 'AnoNasc')) # Vai dar erro quando der o cast(DateType)

df = df.withColumn('Data_Nascimento', concat_ws('-', 'AnoNasc', 'Mes', 'Dia')) # Adaptando Para a Maneira que PySpark aceita

# Finalizando

df.withColumn('Data_Nascimento', col('Data_Nascimento').cast(DateType())).show(4)

df = df.withColumn('Data_Nascimento', col('Data_Nascimento').cast(DateType()))