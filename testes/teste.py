from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg

# Criar sessão Spark
spark = SparkSession.builder.appName("TestePySpark").getOrCreate()

# Criar DataFrame de exemplo
data = [
    ("Alice", 25, 3000.50),
    ("Bob", 30, 4500.75),
    ("Carol", 35, 5000.25),
]
columns = ["nome", "idade", "salario"]
df = spark.createDataFrame(data, columns)

# Transformações: Filtrar, Agregar e Exibir
df_filtered = df.filter(col("idade") > 28)
df_aggregated = df_filtered.groupBy().agg(
    sum("salario").alias("salario_total"),
    avg("salario").alias("salario_medio"),
)

df.show()
df_filtered.show()
df_aggregated.show()

# Salvar DataFrame em um arquivo parquet
df_aggregated.write.mode("overwite").parquet("output/salarios")

# Encerrar sessão Spark
spark.stop()
