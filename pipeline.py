# importing python standard libraries
from pathlib import Path

# importing third party libraries
import pandas as pd

# importing local modules
from etl import calculate_kpi_of_total_sales, extract_and_consolidate_json_files


def main():

    files_path: Path = Path("data")  # defining path

    df_total: pd.DataFrame = extract_and_consolidate_json_files(path=files_path)
    print(df_total)
    df_total_with_total_sales: pd.DataFrame = calculate_kpi_of_total_sales(
        dataframe=df_total
    )
    print(df_total_with_total_sales)


if __name__ == "__main__":
    main()
