# Data Cleaning and Transformation Script


## Overview
This script handles data cleaning and transformation tasks for an online retail dataset. It processes the dataset to handle missing values, filters invalid records, calculates additional metrics, and reformats the data for validation and export.

### Features
#### Handling Missing Data: 
Removes rows with null values.
Data Filtering: Ensures no negative values in the UnitPrice and Quantity columns.


#### Metric Calculation: 
Adds a new column TotalAmount by multiplying UnitPrice and Quantity.

#### Data Validation and Formatting:
Extracts and formats InvoiceDate into separate Invoice_Date and InvoiceTime columns.

#### Converts date and time columns to proper formats.
Export: Writes the cleaned dataset to a CSV file named online_retail(Cleaned).csv.
Script Breakdown
1. Handling Missing Data

d2 = df.drop_nulls()
Removes all rows with missing values to ensure data integrity.

2. Filtering Invalid Records

df3 = df2.filter(pl.col("UnitPrice") > 0)
df3 = df2.filter(pl.col("Quantity") > 0)
Filters out records where UnitPrice or Quantity contains negative values.

3. Calculating Total Amount

df4 = df3.with_columns(pl.col('UnitPrice').mul(pl.col('Quantity')).alias('TotalAmount'))
Adds a TotalAmount column by multiplying UnitPrice and Quantity.

4. Data Validation and Formatting
Extract and Format Date and Time:

df5 = df4.with_columns([
    pl.col("InvoiceDate").dt.strftime("%Y-%m-%d").alias("Invoice_Date"),
    pl.col("InvoiceDate").dt.strftime("%H:%M:%S").alias("InvoiceTime")
])
Separates the InvoiceDate column into:

Invoice_Date (date in YYYY-MM-DD format)
InvoiceTime (time in HH:MM:SS format)
Convert to Proper Formats:

df5 = df5.with_columns([
    pl.col("Invoice_Date").str.to_date(format="%Y-%m-%d").alias("Invoice_Date"),
    pl.col("InvoiceTime").str.strptime(pl.Time, format="%H:%M:%S").alias("InvoiceTime")
])

#### Converts Invoice_Date and InvoiceTime into proper date and time types.

Drop and Rename Columns:


df5 = df5.drop("InvoiceDate")
df5 = df5.with_columns([pl.col("Invoice_Date").alias("InvoiceDate")])
df5 = df5.drop("Invoice_Date")
Cleans up intermediate columns for a consistent schema.

5. Exporting the Cleaned Dataset


df5.write_csv("online_retail(Cleaned).csv")

Exports the cleaned dataset to a CSV file named online_retail(Cleaned).csv.

#### Output
A cleaned and formatted dataset saved as online_retail(Cleaned).csv.
Final columns of the dataset:
python

print(df5.columns)

Displays the cleaned dataset schema.
#### Requirements
Python
Polars library (pip install polars)
