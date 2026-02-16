import pandas as pd

def search_all_sheets():
    try:
        xl = pd.ExcelFile('NAS - PL  Jan 26-KAK.xlsx')
        sheet_names = xl.sheet_names
        
        keywords = ['store', 'spare', 'cwip', 'fa', 'depreciation', 'fixed cost', 'power', 'inventory']
        
        print(f"Searching {len(sheet_names)} sheets...")
        
        found_matches = []
        
        for sheet in sheet_names:
            try:
                df = pd.read_excel('NAS - PL  Jan 26-KAK.xlsx', sheet_name=sheet, header=None)
                # Convert whole dataframe to string for quick search
                # Iterating rows is better for context
                for index, row in df.iterrows():
                    row_str = str(row.values).lower()
                    for k in keywords:
                        if k in row_str:
                            # Capture extraction: Sheet, Row Index, Key Term, Content Snippet
                            found_matches.append((sheet, index, k, row.iloc[0:5].values))
                            break # Move to next row if one keyword found
            except Exception as e:
                print(f"Could not read sheet {sheet}: {e}")

        print("\n--- Top 30 Matches ---")
        for match in found_matches[:30]:
            print(match)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    search_all_sheets()
