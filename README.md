# Azure ETL Data Engineering Project

Hi! This is my First Complete ETL Project Using Azure Services Learning alot of Staff using this Project!

Steps we Will talk About: 
 - Data Ingestion
 - Data Transformation
 - Data Loading
 - Data Reporting
 - End To End Pipline Testing

During This Project I Got alot of bugs and errors everywhere i will discuss what i have remember and screenshoted but if there is a section without a bug discussed that not means it works fine from the first time it was a tough project as a beginner with alot of searching and diving inside documentation.

# Data Ingestion
<p align="center">
  <img src="https://github.com/PeterGeorge7/Azure-ETl-project/blob/main/images/image-removebg-preview.png" alt=""/>
</p>

-   **Database Setup**: I downloaded the AdventureWorksLT2022 Database onto my on-premise SQL Server and created a user with the necessary login credentials, ensuring secure access.
  
<p align="center">
  <img src="https://github.com/PeterGeorge7/Azure-ETl-project/blob/main/images/PipeLine%20Copy%20All%20Tables%20Into%20DataLake/databaseLT.png" alt=""/>
</p>

-   **Azure Key Vault**: To safeguard sensitive information, I set up an Azure Key Vault and stored the SQL Server credentials in the secrets section, enabling seamless integration between Azure services and my on-premise SQL Server.
    
-   **Azure Data Factory**: I created an Azure Data Factory, a fully managed data integration service akin to SSIS. This was a key component for orchestrating the data transfer. Despite not having prior experience with Azure Data Factory, I quickly learned the essential functions and navigated the setup.
    
-   **Troubleshooting**: Throughout the project, I encountered various technical challenges, such as SQL Server connection issues and numerous unexpected errors. Through extensive research and troubleshooting, I was able to resolve these problems and ensure the successful execution of the pipeline.
    
-   **Data Transfer**: I copied all tables from my on-premise SQL Server and created an Azure Storage Account with Data Lake Gen2 capabilities. The table was stored in the Data Lake as a compressed Parquet file (Snappy compression), providing optimized storage and performance.
    
-   **Execution**: After resolving initial errors, I successfully executed the data migration, transferring the data from my on-premise SQL Server to Azure Data Lake Gen2 in a Parquet format.
