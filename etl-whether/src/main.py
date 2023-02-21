from google.cloud import firestore
from google.cloud import bigquery
import pandas as pd
import glob
import json
import datetime


def extract_bq(query: str) -> pd.DataFrame:
    """Query from BigQuery.

    Args:
        query (str): Read from sql file.

    Returns:
        pd.DataFrame: Convert query result to df.
    """
    bq = bigquery.Client()
    res_df = (bq.query(query).result().to_dataframe())
    return res_df


def transform_data(tgt_df: pd.DataFrame) -> dict:
    """Transform to df -> dict.

    Args:
        tgt_df (pd.DataFrame): df to convert to dict.

    Returns:
        pd.DataFrame: Convert dict to df. Option orient='list' is {column -> [values]}.
    """
    return tgt_df.to_dict(orient='list')


def load_fs(collection_name: str, document_name: str, load_data: dict):
    """Load dict to FireStore.

    Args:
        collection_name (str): FireStore collection name.
        document_name (str): Document name of the collection.
        load_data (dict): Data to load into Firestore.
    """
    db = firestore.Client()
    db.collection(collection_name).document(document_name).set(load_data)


def main(data, context):
    query_file_paths = glob.glob('sql/**/*.sql')
    config_file_paths = glob.glob('sql/**/*.json')

    for query_file_path, config_file_path in zip(query_file_paths, config_file_paths):
        query = open(query_file_path).read()
        config = json.loads(open(config_file_path).read())

        res_df = extract_bq(query)
        load_data = transform_data(res_df)
        load_fs(config["collection_name"], str(datetime.date.today()), load_data)