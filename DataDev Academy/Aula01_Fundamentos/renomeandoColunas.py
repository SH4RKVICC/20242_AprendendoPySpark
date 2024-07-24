# Renomenado Todas as Colunas

df = df.withColumnRenamed('Team', 'Selecao').withColumnRenamed('#', 'Numero')\
.withColumnRenamed('FIFA Popular Name', 'Nome_FIFA').withColumnRenamed('Birth Date', 'Nascimento')\
.withColumnRenamed('Shirt Name', 'Nome Camiseta').withColumnRenamed('Club', 'Time').withColumnRenamed('Height', 'Altura')\
.withColumnRenamed('Weight', 'Peso').withColumnRenamed('Pos.', 'Posicao')

df.show(5)

df.columns # Nome das Colunas