# Instalação e Configuração do Apache Spark com PySpark

## Passo 1: Baixar e Extrair o Apache Spark

1. Acesse a página de [downloads do Apache Spark](https://spark.apache.org/downloads.html).
2. Baixe a versão mais recente do Apache Spark.
3. Extraia o arquivo baixado para um diretório de sua preferência.

## Passo 2: Definir Variáveis de Ambiente

1. Abra o terminal.
2. Defina as variáveis de ambiente do Spark:

    ```sh
    export SPARK_HOME=/path/to/spark
    export PATH=$SPARK_HOME/bin:$PATH
    ```

   Substitua `/path/to/spark` pelo caminho onde você extraiu o Apache Spark.

## Passo 3: Instalar o PySpark

1. No terminal, execute o comando:

    ```sh
    pip install pyspark
    ```

## Passo 4: Configurar o Visual Studio Code

1. Abra o Visual Studio Code.
2. Instale a extensão do Python:
   - Vá para o menu de extensões (ícone de quadrado no lado esquerdo).
   - Procure por "Python" e instale a extensão fornecida pela Microsoft.
3. Selecione o interpretador Python correto:
   - Pressione `Ctrl+Shift+P` (ou `Cmd+Shift+P` no macOS) para abrir a Paleta de Comandos.
   - Digite `Python: Select Interpreter` e escolha o interpretador Python onde o PySpark está instalado.
