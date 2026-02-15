import pandas as pd
import glob
import os
import pandera as pa
from pathlib import Path

def extract_data(folder: str) -> pd.DataFrame:
    files_json = glob.glob(os.path.join(folder, '*.json'))
    df_list = [pd.read_json(file) for file in files_json]
    df_final = pd.concat(df_list, ignore_index=True)
    return df_final

def transform_data(df: pd.DataFrame):
    df['Receita'] = df['Quantidade'] * df['Venda']
    print(df)
    return df


if __name__ == "__main__":
    data = extract_data('data')
    transform_data(data)

