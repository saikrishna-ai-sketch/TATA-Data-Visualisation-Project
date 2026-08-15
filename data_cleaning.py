"""
Tata Forage Data Visualisation - Data Cleaning Workflow

This script processes the Online Retail dataset following the Tata Forage specifications:
1. Ensures Quantity is greater than or equal to 1 (Quantity >= 1).
2. Ensures UnitPrice is greater than or equal to 0 (UnitPrice >= 0).
3. Verifies data types, missing values, and calculated Revenue.
4. Exports the verified dataset to 'cleaned_online_retail.csv'.
"""

import os
import sys
import pandas as pd

INPUT_FILE = "Online_Retail_Cleaned.csv"
OUTPUT_FILE = "cleaned_online_retail.csv"

def run_cleaning_pipeline(input_path: str, output_path: str):
    """
    Executes the data cleaning workflow according to Tata Forage requirements.
    """
    print("=" * 60)
    print("TATA FORAGE DATA VISUALISATION - DATA CLEANING PIPELINE")
    print("=" * 60)

    # 1. Check Input File Existence
    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' not found.")
        sys.exit(1)

    print(f"[1/5] Loading dataset from '{input_path}'...")
    df_raw = pd.read_csv(input_path, low_memory=False)
    initial_rows, initial_cols = df_raw.shape
    print(f"      Initial dataset shape: {initial_rows:,} rows, {initial_cols} columns")

    # 2. Inspect Columns and Data Types
    print("\n[2/5] Inspecting columns and data types:")
    for col in df_raw.columns:
        print(f"      - {col:15s}: {str(df_raw[col].dtype):10s} (Nulls: {df_raw[col].isnull().sum():,})")

    # 3. Apply Tata Forage Cleaning Rules
    print("\n[3/5] Applying Tata Forage cleaning rules:")
    
    # Rule 1: Quantity >= 1
    invalid_qty_count = (df_raw['Quantity'] < 1).sum()
    print(f"      - Quantity < 1 check : {invalid_qty_count:,} invalid rows found.")
    
    # Rule 2: UnitPrice >= 0
    invalid_price_count = (df_raw['UnitPrice'] < 0).sum()
    print(f"      - UnitPrice < 0 check: {invalid_price_count:,} invalid rows found.")

    # Filter dataframe strictly based on Tata Forage instructions
    df_cleaned = df_raw[(df_raw['Quantity'] >= 1) & (df_raw['UnitPrice'] >= 0)].copy()

    # Calculate / Verify Revenue column (Quantity * UnitPrice)
    df_cleaned['Revenue'] = (df_cleaned['Quantity'] * df_cleaned['UnitPrice']).round(2)

    cleaned_rows = len(df_cleaned)
    removed_rows = initial_rows - cleaned_rows
    print(f"      Rows before cleaning: {initial_rows:,}")
    print(f"      Rows after cleaning : {cleaned_rows:,}")
    print(f"      Rows removed        : {removed_rows:,}")

    # 4. Export Cleaned Dataset
    print(f"\n[4/5] Exporting cleaned dataset to '{output_path}'...")
    df_cleaned.to_csv(output_path, index=False)
    file_size_mb = os.path.getsize(output_path) / (1024 * 1024)
    print(f"      Export successful! File size: {file_size_mb:.2f} MB")

    # 5. Verification Phase
    print("\n[5/5] Verifying exported dataset:")
    df_verify = pd.read_csv(output_path, low_memory=False)
    print(f"      Verified shape        : {df_verify.shape[0]:,} rows, {df_verify.shape[1]} columns")
    print(f"      Quantity Min / Max    : {df_verify['Quantity'].min()} / {df_verify['Quantity'].max()}")
    print(f"      UnitPrice Min / Max   : {df_verify['UnitPrice'].min()} / {df_verify['UnitPrice'].max()}")
    print(f"      Missing CustomerIDs   : {df_verify['CustomerID'].isnull().sum():,}")
    print(f"      Missing Descriptions  : {df_verify['Description'].isnull().sum():,}")

    assert df_verify['Quantity'].min() >= 1, "Verification Failed: Quantity < 1 detected!"
    assert df_verify['UnitPrice'].min() >= 0.0, "Verification Failed: UnitPrice < 0 detected!"
    assert len(df_verify) == cleaned_rows, "Verification Failed: Row count mismatch!"

    print("\n" + "=" * 60)
    print("DATA CLEANING PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 60)

if __name__ == "__main__":
    run_cleaning_pipeline(INPUT_FILE, OUTPUT_FILE)
