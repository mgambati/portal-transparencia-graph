import pandas as pd
from pathlib import Path
from neo4j import GraphDatabase
import json
import re
import neotime
import random
from tqdm import tqdm

pd.set_option("display.expand_frame_repr", False)


def to_camel(snake_str):
    first, *others = re.split("_| ", snake_str)
    return "".join([first.lower(), *map(str.title, others)])


def to_neotime_date(value):
    if pd.isnull(value):
        return None

    return neotime.Date(value.year, value.month, value.day)


def load_dataset(name, load_subset=False, subset_amount=1000):
    file_path = Path("./src/DadosPortalTransparencia/201908_" + name + ".csv").resolve()

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


def create_db_connection():
    return GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "22caramelo"))


def run_queries(df, query_creator, desc):
    with create_db_connection() as driver:
        n = len(df.index)
        step = 1000
        pbar = tqdm(total=n, desc=desc)

        for i in range(0, n, step):
            sliced_df = df.iloc[i : i + step]

            with driver.session() as session:
                tx = session.begin_transaction()
                for _, row in sliced_df.iterrows():
                    query_creator(tx, row)
                tx.commit()
                pbar.update(step)

        pbar.close()


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
