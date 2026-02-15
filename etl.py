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
    return df

def load_data(df: pd.DataFrame, formarts: list):
    for format in formarts:
        if format == 'csv':
            df.to_csv('data.csv',index=False)
        elif format == 'parquet':
            df.to_parquet('data.parquet',index=False)


if __name__ == "__main__":
    data = extract_data('data')
    data_transformed = transform_data(data)
    load_data(data_transformed, ['csv'])

