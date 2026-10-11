import pandas as pd
from pathlib import Path

# Step 1: Find the CSV file
project_folder = Path(__file__).resolve().parent.parent
file_path = project_folder / "Data" / "food_delivery_orders.csv"

# Step 2: Load the dataset
df = pd.read_csv(file_path)

# Step 3: Display the first 5 rows
print("FIRST 5 ROWS:")
print(df.head())

# Step 4: Check rows and columns
print("\nDATASET SHAPE:")
print(df.shape)

# Step 5: Check missing values
print("\nMISSING VALUES:")
print(df.isnull().sum())

# Step 6: Check duplicate records
print("\nDUPLICATE ROWS:")
print(df.duplicated().sum())

# Step 7: Check data types
print("\nDATA TYPES:")
print(df.dtypes)



# STEP 8: Make a copy of the original data
clean_df = df.copy()

# STEP 9: Remove duplicate rows
clean_df = clean_df.drop_duplicates()

# STEP 10: Remove extra spaces from column names
clean_df.columns = clean_df.columns.str.strip()

# STEP 11: Convert order date to datetime
clean_df["order_date"] = pd.to_datetime(
    clean_df["order_date"],
    errors="coerce"
)

# STEP 12: Convert numeric columns
numeric_columns = [
    "order_amount",
    "total_amount",
    "delivery_time_minutes"
]

for col in numeric_columns:
    clean_df[col] = pd.to_numeric(
        clean_df[col],
        errors="coerce"
    )

# STEP 13: Remove rows missing essential information
clean_df = clean_df.dropna(
    subset=[
        "order_id",
        "order_date",
        "total_amount"
    ]
)

# STEP 14: Remove invalid negative amounts
clean_df = clean_df[
    clean_df["total_amount"] >= 0
]

# STEP 15: Check the cleaned data
print("\nCLEANED DATASET:")
print(clean_df.shape)

print("\nMISSING VALUES AFTER CLEANING:")
print(clean_df.isnull().sum())

# STEP 16: Save the cleaned dataset
output_path = project_folder / "data" / "cleaned_food_delivery.csv"

clean_df.to_csv(output_path, index=False)

print("\nData cleaning completed!")
print("Saved file:", output_path)
