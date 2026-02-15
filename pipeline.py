from etl import pipeline_run
from pathlib import Path

if __name__ == "__main__":
    root_folder = Path(__file__).parent
    file_path = root_folder / 'data'
    output_format = 'csv'

    pipeline_run(file_path,output_format)