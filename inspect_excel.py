import pandas as pd

file_path = "NAS - PL  Jan 26-KAK.xlsx"

# Load the P&L sheet to see headers and structure for accurate mapping
try:
    df = pd.read_excel(file_path, sheet_name="P&L H V1", header=None) # Read without header to see raw layout
    print("Preview of 'P&L H V1':")
    print(df.head(20).to_markdown())
except Exception as e:
    print(f"Error reading excel: {e}")
