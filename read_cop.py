import pandas as pd
try:
    df = pd.read_excel('NAS - PL  Jan 26-KAK.xlsx', sheet_name='COP', header=None)
    # Get first 60 rows and 15 columns to capture the structure
    preview = df.iloc[0:60, 0:15]
    with open('cop_sheet_preview.md', 'w') as f:
        f.write(preview.to_markdown(index=False))
    print("Successfully wrote cop_sheet_preview.md")
except Exception as e:
    print(f"Error: {e}")
