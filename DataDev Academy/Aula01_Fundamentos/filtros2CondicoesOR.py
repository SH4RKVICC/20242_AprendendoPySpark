df.filter((col('Nome_FIFA') == 'MESSI Lionel') | (col('Nome_FIFA') == 'SALVIO Eduardo') | (col('Altura') == 199)).show()