# CONCAT une informações de duas ou mais colunas em uma só

df.withColumn('Concat', concat('Selecao', 'Nome Camiseta')).show(3) # Sem espaço separador

df.withColumn('Separador', concat_ws(' - ','Numero', 'Nome Camiseta', 'Posicao')).show(2) # Com espaço separador