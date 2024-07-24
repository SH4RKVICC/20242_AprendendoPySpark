# Filtrando jogadores da Argentina com Altura m> 180
df.filter((col('Selecao') == 'Argentina') & (col('Altura') > 180)).show(8)

# Filtrando jogadores do Brasil com altura > 180 e peso > 80
df.filter((col('Selecao') == 'Brazil') & (col('Altura') > 180) & (col('Peso') >= 80)).show()

# Filtrando jogadores da Franca com altura > 190 e peso > 90
df.filter((col('Selecao') == 'France') & (col('Altura') > 190) & (col('Peso') > 90)).show()

## Outra Maneira de Fazer

df.filter('Selecao == "Brazil"').filter(col('Numero') > 20).show(3)