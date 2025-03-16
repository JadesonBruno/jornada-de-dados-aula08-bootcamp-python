from etl import pipeline_to_calculate_consolidated_sales_kpi


def main():
    pipeline_to_calculate_consolidated_sales_kpi(
        files_path="data", files_type_to_export=["csv", "parquet"]
    )


if __name__ == "__main__":
    main()
