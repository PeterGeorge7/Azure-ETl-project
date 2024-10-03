USE gold_db
GO CREATE
    OR ALTER PROCEDURE sp_CreateSqlServerViewForAllTables @ViewName nvarchar(100) AS BEGIN
DECLARE @statment VARCHAR(MAX)
SET @statment = N'CREATE OR ALTER VIEW ' + @ViewName + ' AS
                        SELECT * FROM OPENROWSET(
                        BULK ''https://project1storageaccount.dfs.core.windows.net/gold/SalesLT/' + @ViewName + '/'',
                        FORMAT = ''DELTA''
                        ) as [result]' EXEC (@statment)
end
GO