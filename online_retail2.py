import pandas as pd
import polars as pl
from datetime import datetime

df=pl.read_excel(source="/content/Online Retail.xlsx", infer_schema_length=None)


#handling missing data.
df2=df.drop_nulls()

#filter quantity and unit price column as both cannot carry a negative value.
df3=df2.filter(pl.col("UnitPrice") > 0)
df3=df2.filter(pl.col("Quantity") > 0)

#getting the total amountwhen quantity is multiplied ny unit price
df4=df3.with_columns(pl.col('UnitPrice').mul(pl.col('Quantity')).alias('TotalAmount'))


#Data Validation
df5 = df4.with_columns([
    pl.col("InvoiceDate").dt.strftime("%Y-%m-%d").alias("Invoice_Date"),
    pl.col("InvoiceDate").dt.strftime("%H:%M:%S").alias("InvoiceTime") 
])

df5 = df5.with_columns([
    pl.col("Invoice_Date").str.to_date(format="%Y-%m-%d").alias("Invoice_Date"), 
    pl.col("InvoiceTime").str.strptime(pl.Time, format="%H:%M:%S").alias("InvoiceTime") 
])

df5=df5.drop("InvoiceDate")

df5 = df5.with_columns([pl.col("Invoice_Date").alias("InvoiceDate")])

df5=df5.drop("Invoice_Date")

print(df5.columns)

df5.write_csv("online_retail(Cleaned).csv")