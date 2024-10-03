# Databricks notebook source
# MAGIC %md
# MAGIC ## transform column names for all tables

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

gold_file_path = "abfss://gold@project1storageaccount.dfs.core.windows.net/"
silver_file_path = "abfss://silver@project1storageaccount.dfs.core.windows.net/"

# COMMAND ----------

# get silver table names
silver_tables = []
for table in dbutils.fs.ls(silver_file_path + "SalesLT/"):
    silver_tables.append(table.name.split("/")[0])

# COMMAND ----------

for table in silver_tables:
    address_df = silver_file_path + "SalesLT/" + table + "/"
    df = spark.read.format("delta").load(address_df)
    column_names = df.columns
    for old_column_name in column_names:
        new_column_name = "".join(["_" + char if char.isupper() and not old_column_name[i-1].isupper() else char for i,char in enumerate(old_column_name)]).lstrip("_")
        df = df.withColumnRenamed(old_column_name, new_column_name)
    
    gold_file_path = "abfss://gold@project1storageaccount.dfs.core.windows.net/"
    df.write.format("delta").mode("overwrite").save(gold_file_path + "SalesLT/" + table + "/")


