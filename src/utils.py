import pandas as pd
from pathlib import Path
import json
import re
import neotime
import random
from tqdm import tqdm

# pd.set_option("display.expand_frame_repr", False)


def to_camel(snake_str):
    first, *others = re.split("_| ", snake_str)
    return "".join([first.lower(), *map(str.title, others)])


def to_neotime_date(value):
    if pd.isnull(value):
        return None

    return neotime.Date(value.year, value.month, value.day)


def load_dataset(name, load_subset=False, subset_amount=1000):
    file_path = Path("./data/201908_" + name + ".csv").resolve()

    if load_subset is False:
        df = pd.read_csv(
            file_path,
            sep=";",
            encoding="latin1",
            dtype=str
        )
        df.columns = df.columns.str.lower()
        return df

    number_of_entries = sum(1 for line in open(file_path, encoding="latin-1")) - 1

    skip = sorted(
        random.sample(
            range(1, number_of_entries + 1), number_of_entries - subset_amount
        )
    )

    df = pd.read_csv(
        file_path,
        sep=";",
        encoding="latin1",
        dtype=str,
        skiprows=skip if load_subset is True else None,
    )
    df.columns = df.columns.str.lower()

    return df


def column_to_float(original_df, column):
    df = original_df.copy()
    df[column] = df[column].str.replace(",", ".")
    df[column] = df[column].astype(float)

    return df


def column_to_int(original_df, column):
    df = original_df.copy()
    df[column] = df[column].astype(int)

    return df


def column_to_datetime(original_df, column):
    df = original_df.copy()
    df[column] = pd.to_datetime(df[column], dayfirst=True)

    return df
