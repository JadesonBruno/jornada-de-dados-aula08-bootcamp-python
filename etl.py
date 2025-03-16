# import python standard libraries
import glob
import os
from pathlib import Path

# importing third party libraries
import pandas as pd


# function to extract and cosolidate json file
def extract_and_consolidate_json_files(path: Path) -> pd.DataFrame:
    json_files = glob.glob(os.path.join(path, "*.json"))

    dataframes_list = [pd.read_json(json_file) for json_file in json_files]
    df_total = pd.concat(dataframes_list, ignore_index=True)

    return df_total
