# Filtrar DF

df.filter('Selecao = "Brazil"').show(7) # Filtrando selecao que corresponde a Brasil

# Mostrando Que NomesColunas com espaço dão erro

df.filter('Nome Camiseta = "Fred"').show() #Vai dar erro

# Mostrando como filtrar de maneira correta colunas com espaço

df.filter(col('Nome Camiseta') == 'FRED').show()