spark = (
    SparkSession.builder
    .master('local') # Informando o master porque o Spark trabalha com Clusterização.
    .appName('SH4RKVICC_spark') # Nome da Sessão, posso colocar o nome que quiser.
    .getOrCreate() # Caso você tenha criado anteriormente, ele ira puxar, caso não, criara uma nova.
)