from tqdm import tqdm
from neo4j import GraphDatabase


def connect():
    return GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "22caramelo"))


def run_queries(df, query_creator, desc):
    with connect() as driver:
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

