# import python standard libraries
from pathlib import Path

# import local modules
from etl import extract_and_consolidate_json_files


def main():

    files_path = Path("data")  # defining path

    print(extract_and_consolidate_json_files(path=files_path))


if __name__ == "__main__":
    main()
