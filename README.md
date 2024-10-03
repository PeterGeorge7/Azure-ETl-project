# Azure ETL Data Engineering Project

Hi! This is my First Complete ETL Project Using Azure Services Learning alot of Staff using this Project!

Steps we Will talk About: 
 - [Data Ingestion](#data-ingestion)
 - [Data Transformation](#Data-Transformation)
 - [Data Loading](#Data-Loading)
 - [Data Reporting](#Data-Reporting)
 - [End To End Pipline Testing](#End-To-End-Pipline-Testing)

During This Project I Got alot of bugs and errors everywhere i will discuss what i have remember and screenshoted but if there is a section without a bug discussed that not means it works fine from the first time it was a tough project as a beginner with alot of searching and diving inside documentation. (Codes Provided in Repo)

# Data Ingestion
<p align="center">
  <img src="https://github.com/PeterGeorge7/Azure-ETl-project/blob/main/images/Ingestion.png" alt=""/>
</p>

-   **Database Setup**: I downloaded the AdventureWorksLT2022 Database onto my on-premise SQL Server and created a user with the necessary login credentials, ensuring secure access.
  
<p align="center">
  <img src="https://github.com/PeterGeorge7/Azure-ETl-project/blob/main/images/PipeLine%20Copy%20All%20Tables%20Into%20DataLake/databaseLT.png" alt=""/>
</p>

-   **Azure Key Vault**: To safeguard sensitive information, I set up an Azure Key Vault and stored the SQL Server credentials in the secrets section, enabling seamless integration between Azure services and my on-premise SQL Server.

 <p align="center">
  <img src="https://github.com/PeterGeorge7/Azure-ETl-project/blob/main/images/PipeLine%20Copy%20All%20Tables%20Into%20DataLake/keyvault.png" alt=""/>
</p>
    
-   **Azure Data Factory**: I created an Azure Data Factory, a fully managed data integration service akin to SSIS. This was a key component for orchestrating the data transfer. Despite not having prior experience with Azure Data Factory, I quickly learned the essential functions and navigated the setup.

 <p align="center">
  <img src="https://github.com/PeterGeorge7/Azure-ETl-project/blob/main/images/PipeLine%20Copy%20All%20Tables%20Into%20DataLake/PipeLine.png" alt=""/>
</p>  
<p align="center">
 Pipline
</p> 


 <p align="center">
  <img src="https://github.com/PeterGeorge7/Azure-ETl-project/blob/main/images/PipeLine%20Copy%20All%20Tables%20Into%20DataLake/Query%20To%20Get%20All%20scheme%20names%20and%20table%20name%20from%20the%20data%20base%20in%20the%20Lookup%20task.png" alt=""/>
</p>  
<p align="center">
  Query To Get All scheme names and table name from the data base in the Lookup task
</p> 

 <p align="center">
  <img src="https://github.com/PeterGeorge7/Azure-ETl-project/blob/main/images/PipeLine%20Copy%20All%20Tables%20Into%20DataLake/output%20of%20the%20lookup%20(that%20i%20will%20use%20to%20SELECT%20data%20from%20it).png" alt=""/>
</p>  
<p align="center">
  output of the lookup (that i will use to SELECT data from it)
</p>  

 <p align="center">
  <img src="https://github.com/PeterGeorge7/Azure-ETl-project/blob/main/images/PipeLine%20Copy%20All%20Tables%20Into%20DataLake/create%20Copy%20Data%20in%20the%20foreach.png" alt=""/>
</p>  
  <p align="center">
  create Copy Data in the foreach
</p> 

 <p align="center">
  <img src="https://github.com/PeterGeorge7/Azure-ETl-project/blob/main/images/PipeLine%20Copy%20All%20Tables%20Into%20DataLake/Source%20for%20the%20Copy%20Data%20Task.png" alt=""/>
</p>  
 <p align="center">
  Source for the Copy Data Task
</p>  

 <p align="center">
  <img src="https://github.com/PeterGeorge7/Azure-ETl-project/blob/main/images/PipeLine%20Copy%20All%20Tables%20Into%20DataLake/sink%20is%20parquet%20file%20inside%20the%20data%20lake.png" alt=""/>
</p>  
 <p align="center">
  Sink for the Copy Data Task
</p>  


 <p align="center">
  <img src="https://github.com/PeterGeorge7/Azure-ETl-project/blob/main/images/PipeLine%20Copy%20All%20Tables%20Into%20DataLake/so%20sink%20here%20needs%20to%20give%20the%20the%20value%20of%20this%20parametes%20(which%20i%20get%20the%20from%20lookup).png" alt=""/>
</p>  
 <p align="center">
  so sink here needs to give the the value of this parametes (which i get the from lookup)
</p>  
  
-   **Troubleshooting**: Throughout the project, I encountered various technical challenges, such as SQL Server connection issues and numerous unexpected errors. Through extensive research and troubleshooting, I was able to resolve these problems and ensure the successful execution of the pipeline.
    
-   **Data Transfer**: I copied all tables from my on-premise SQL Server and created an Azure Storage Account with Data Lake Gen2 capabilities. The table was stored in the Data Lake as a compressed Parquet file (Snappy compression), providing optimized storage and performance.
    
-   **Execution**: After resolving initial errors, I successfully executed the data migration, transferring the data from my on-premise SQL Server to Azure Data Lake Gen2 in a Parquet format.

 <p align="center">
  <img src="https://github.com/PeterGeorge7/Azure-ETl-project/blob/main/images/PipeLine%20Copy%20All%20Tables%20Into%20DataLake/Copied.png" alt=""/>
</p>  
 <p align="center">
 Data Successfully copied to Data Lake Bronze Layer Container
</p>  



# Data Transformation

 <p align="center">
  <img src="https://github.com/PeterGeorge7/Azure-ETl-project/blob/main/images/Transfor.png" alt=""/>
</p>  
 <p align="center">
 Project Update
</p>  

Once the data was ingested into the Data Lake, the next step was **Data Transformation**. For this, I used **Databricks** to implement a **Lakehouse architecture** with **medallion layers**: Bronze, Silver, and Gold. Each layer in this architecture serves a specific purpose:

 <p align="center">
  <img src="https://github.com/PeterGeorge7/Azure-ETl-project/blob/main/images/Transformation/databricks%20computer%20instance.png" alt=""/>
</p>  
 <p align="center">
 Create New Databricks Compute to use
</p>  

 <p align="center">
  <img src="https://github.com/PeterGeorge7/Azure-ETl-project/blob/main/images/Transformation/connect%20databricks%20with%20storage%20gen2.png" alt=""/>
</p>  
 <p align="center">
 Connecting out Compute to Data lake Gen2
</p>  

1. **Bronze Layer**  
   Raw data was stored in the Bronze layer, directly from the ingestion step. This unprocessed data serves as the foundation for all subsequent transformations.
 [SHOW CODE](https://github.com/PeterGeorge7/Azure-ETl-project/blob/main/bronze%20to%20silver.py)

2. **Silver Layer**  
   In the Silver layer, I applied data cleansing and transformation processes. Using Databricks notebooks, I handled tasks such as removing duplicates, standardizing formats, and enriching the data by joining tables from multiple sources.
   [SHOW CODE](https://github.com/PeterGeorge7/Azure-ETl-project/blob/main/silver%20to%20gold.py)

 <p align="center">
  <img src="https://github.com/PeterGeorge7/Azure-ETl-project/blob/main/images/Transformation/transform%20the%20datetime%20type%20to%20date%20and%20save%20the%20delta%20files%20in%20datalake.png" alt=""/>
</p>  
 <p align="center">
 transform the datetime type to date and save the delta files in lakehouse
</p>  

3. **Gold Layer**  
   The final Gold layer contains refined, analytics-ready data. This is where the data is optimized for reporting and querying. Complex aggregations, business logic, and data models were applied here to prepare the data for use in **Power BI** and other reporting tools.
   [SHOW CODE](https://github.com/PeterGeorge7/Azure-ETl-project/blob/main/silver%20to%20gold.py)

 <p align="center">
  <img src="https://github.com/PeterGeorge7/Azure-ETl-project/blob/main/images/Transformation/transform%20column%20names%20and%20save%20the%20delta%20files%20in%20datalake%20in%20gold%20layer.png" alt=""/>
</p>  
 <p align="center">
 transform column names and save the delta files in datalake in gold layer
</p>  


 <p align="center">
  <img src="https://github.com/PeterGeorge7/Azure-ETl-project/blob/main/images/building-data-pipelines-with-delta-lake-120823.png" alt=""/>
</p>  
 <p align="center">
 building data pipelines using Medallion Arch
</p> 

> _Challenges Faced:_  
   Setting up the data transformations in Databricks presented several challenges. The most significant issues I encountered were related to connecting Databricks with Azure Data Lake Gen2. I faced authentication errors when configuring the access controls, especially with setting up the appropriate service principal and managing permissions. Another frequent issue was with inconsistent read/write operations, where Databricks jobs failed due to mismatches in file formats or schema changes. Debugging these connection issues and permission errors required deep dives into documentation and community forums.


# Data Loading

 <p align="center">
  <img src="https://github.com/PeterGeorge7/Azure-ETl-project/blob/main/images/load%20phase.png" alt=""/>
</p>  
 <p align="center">
 Project Update
</p>  

For the **Data Loading** phase, I moved the data from the **Gold layer** in Azure Data Lake Storage Gen2 to **Azure Synapse Analytics**. Instead of loading raw data into Synapse, I created **SQL Server views** from the **Delta format** data stored in the Gold layer. This allowed me to access the refined, analytics-ready data directly from Synapse without having to copy or physically move the data.


 <p align="center">
  <img src="https://github.com/PeterGeorge7/Azure-ETl-project/blob/main/images/Load/Load%20Pipline.png" alt=""/>
</p>  
 <p align="center">
 Load Pipline in Azure Synapse
</p> 


## Steps Involved:
1. **Get Metadata from Gold Layer**  
   I first retrieved the necessary metadata from the Gold layer of the Data Lake using Azure Data Factory. This metadata was crucial in ensuring the right tables and data formats were accessed in Synapse.

2. **ForEach Activity in Azure Data Factory**  
   A **ForEach** activity was used to loop through the tables in the Gold layer and dynamically create views in Synapse for each one.

3. **Creating Views in Synapse**  
   In Synapse, I used a stored procedure (`sp_CreateSqlServerViewForAllTables`) to create SQL Server views. These views accessed the data from the **Gold layer** via an `OPENROWSET` query, reading the data stored in **Delta format**. Here’s an example of how the views were dynamically generated:
   
 <p align="center">
  <img src="https://github.com/PeterGeorge7/Azure-ETl-project/blob/main/images/Load/Stored%20Procedure.png" alt=""/>
</p>  
 <p align="center">
 Create Views Stored Procedure
</p> 

[SHOW CODE](https://github.com/PeterGeorge7/Azure-ETl-project/blob/main/sp_CreateSqlServerViewForAllTables.sql)

# Data Reporting

For the **Data Reporting** phase, I used the views created in the **Azure Synapse Analytics** database to perform data analysis. These views were directly connected to the **Gold layer** of the Azure Data Lake, ensuring that I was working with the final, refined data. By accessing the data via views, I could easily pull the necessary information for reporting without duplicating storage or moving large datasets.


 <p align="center">
  <img src="https://github.com/PeterGeorge7/Azure-ETl-project/blob/main/images/Report/PowerBI.png" alt=""/>
</p>  
 <p align="center">
PowerBI Analysis
</p>

## Steps Involved:
1. **Connecting Power BI to Synapse**  
   I connected **Power BI** to the **Synapse database** where the views were created. Power BI allowed me to directly query the views, which were based on the Delta format data stored in the Gold layer. This connection provided a seamless way to visualize and analyze the refined data.

2. **Building Reports in Power BI**  
   Using the data from these views, I built interactive dashboards and reports in Power BI. The views provided a consistent structure for my data, allowing for easy creation of:
   - **Aggregated metrics**
   - **Visual charts** (bar charts)
   - **Custom calculations** based on business requirements

3. **Benefits of Using Views**  
   By using views in Synapse, I ensured that:
   - **Real-time data access**: Since the views were dynamically generated from the Gold layer, any updates to the data were reflected instantly in Power BI reports.
   - **Efficient querying**: With the **Delta format** in place, query performance was optimized, making the reporting process faster and more efficient.
   - **Simplified data management**: There was no need to copy data between systems, reducing complexity and ensuring that data in reports was always up-to-date.

> _Note:_  
   While setting up the connection between Power BI and Synapse, I encountered some **connection string issues** and **authentication challenges**, which were resolved by ensuring the correct access policies were in place and verifying the credentials in Azure.



# End To End Pipline Testing
In this video, I demonstrate the end-to-end data pipeline, starting with inserting two new records into the **on-premise SQL Server database**. The **Azure Data Factory (ADF)** pipeline is triggered automatically based on a **5-minute interval trigger**.

## Workflow Overview:

[Watch the Video Here](https://youtu.be/IHUMCjygIEI)

1. **Data Insertion:**
   - Two new records are added to the **on-premise SQL Server**.
   
2. **ADF Pipeline Execution:**
   - The ADF pipeline, which is scheduled to run every 5 minutes, detects the new records and begins the process of data ingestion.
   - The pipeline moves the new records to **Azure Data Lake (Gold Layer)** and creates the necessary transformations.

3. **Data Visibility in Power BI:**
   - Once the records are loaded and transformed, they are available in **Azure Synapse** through views, which are queried in **Power BI** for analysis and reporting.
   - The new records can be visualized in **Power BI**, confirming that the end-to-end pipeline works as expected.
