import pandas as pd
import zipfile
import os
import sys


def csvs_to_excel(zip_file_path, output_excel_path):
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_excel_path), exist_ok=True)

    with pd.ExcelWriter(output_excel_path, engine='openpyxl') as writer:
        with zipfile.ZipFile(zip_file_path, 'r') as z:
            for csv_file in z.namelist():
                with z.open(csv_file) as f:
                    df = pd.read_csv(f)

                sheet_name = os.path.splitext(csv_file)[0]
                df.to_excel(writer, sheet_name=sheet_name, index=False)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <zip_file_path>")
        sys.exit(1)

    zip_file_path = sys.argv[1]
    output_excel_path = os.path.splitext(zip_file_path)[0] + '.xlsx'

    csvs_to_excel(zip_file_path, output_excel_path)
    print(f"Excel file created: {output_excel_path}")