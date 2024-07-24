df = spark.read.csv('wc2018-players.csv', header=True, inferSchema=True)

# se não colocar o inferSchema, PySparl lerá todas as colunas como String

df.show(5) # Exibir DF