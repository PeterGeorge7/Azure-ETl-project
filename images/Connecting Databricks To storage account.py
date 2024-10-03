# Databricks notebook source
service_credential = dbutils.secrets.get(scope="key-vault-secret",key="databricks-vault1")

spark.conf.set("fs.azure.account.auth.type.project1storageaccount.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.project1storageaccount.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.project1storageaccount.dfs.core.windows.net", "0d799745-63fb-431e-8ecd-7ec7a6a1da00")
spark.conf.set("fs.azure.account.oauth2.client.secret.project1storageaccount.dfs.core.windows.net", service_credential)
spark.conf.set("fs.azure.account.oauth2.client.endpoint.project1storageaccount.dfs.core.windows.net", "https://login.microsoftonline.com/0bc92751-071a-4e2c-a48b-633206fef374/oauth2/token")
spark.conf.set("fs.azure.account.oauth2.client.secret.project1storageaccount.dfs.core.windows.net", "ZsS8Q~vX6xD6YL6eavi8v0xTUzfflijXQl.SKbME")
