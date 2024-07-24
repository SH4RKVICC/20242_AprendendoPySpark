# Testando Mudança
df.withColumn('AnoNasc', col('AnoNasc').cast(IntegerType())).show(5)

# Implementando Mudança na Tabela 
df = df.withColumn('AnoNasc', col('AnoNasc').cast(IntegerType()))