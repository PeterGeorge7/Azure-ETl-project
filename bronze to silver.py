# Databricks notebook source
# MAGIC %md
# MAGIC ## Transform All Tables

# COMMAND ----------

service_credential = dbutils.secrets.get(scope="key-vault-secret",key="databricks-vault1")

spark.conf.set("fs.azure.account.auth.type.project1storageaccount.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.project1storageaccount.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.project1storageaccount.dfs.core.windows.net", "0d799745-63fb-431e-8ecd-7ec7a6a1da00")
spark.conf.set("fs.azure.account.oauth2.client.secret.project1storageaccount.dfs.core.windows.net", service_credential)
spark.conf.set("fs.azure.account.oauth2.client.endpoint.project1storageaccount.dfs.core.windows.net", "https://login.microsoftonline.com/0bc92751-071a-4e2c-a48b-633206fef374/oauth2/token")

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.project1storageaccount.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.project1storageaccount.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.project1storageaccount.dfs.core.windows.net", "0d799745-63fb-431e-8ecd-7ec7a6a1da00")
spark.conf.set("fs.azure.account.oauth2.client.secret.project1storageaccount.dfs.core.windows.net", "ZsS8Q~vX6xD6YL6eavi8v0xTUzfflijXQl.SKbME")
spark.conf.set("fs.azure.account.oauth2.client.endpoint.project1storageaccount.dfs.core.windows.net", "https://login.microsoftonline.com/0bc92751-071a-4e2c-a48b-633206fef374/oauth2/token")


# COMMAND ----------

from pyspark.sql.functions import to_date, date_format
bronze_path = "abfss://bronze@project1storageaccount.dfs.core.windows.net/"
silver_file_path = "abfss://silver@project1storageaccount.dfs.core.windows.net/"

# COMMAND ----------

tables_name =[]
for table in dbutils.fs.ls(bronze_path + "SalesLT/"):
    tables_name.append(table.name.split("/")[0])

# COMMAND ----------


for table in tables_name:
    df = spark.read.format("parquet").load(bronze_path + "SalesLT/" +table + "/" + table + ".parquet")
    columns = df.columns
    for column in columns:
        if "Date" in column or "date" in column:
            df = df.withColumn(column, to_date(date_format(column, "yyyy-MM-dd")))
    
    file_destination = silver_file_path + "SalesLT/" + table + "/"
    df.write.mode("overwrite").format("delta").save(file_destination)

