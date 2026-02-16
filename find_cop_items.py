import pandas as pd

def search_cop():
    try:
        df = pd.read_excel('NAS - PL  Jan 26-KAK.xlsx', sheet_name='COP', header=None)
        
        keywords = ['store', 'spare', 'cwip', 'fa', 'depreciation', 'fixed', 'power', 'electr']
        
        print(f"Total rows in COP sheet: {len(df)}")
        
        found_rows = []
        for index, row in df.iterrows():
            row_str = str(row.values).lower()
            for k in keywords:
                if k in row_str:
                    found_rows.append((index, row.iloc[0:5].values)) # Keep it brief
                    break
        
        print("\n--- Found Items ---")
        for idx, content in found_rows:
            print(f"Row {idx}: {content}")
            
        # Also print rows 60-120 to see what was missed after the first extracted batch
        print("\n--- Rows 60-100 Preview ---")
        print(df.iloc[60:100, 0:5].to_markdown())

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    search_cop()
