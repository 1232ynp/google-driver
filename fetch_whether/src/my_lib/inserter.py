import pandas as pd
import pandas_gbq


def insert_bq(df: pd.DataFrame, dataset_name: str, project_id: str, table_schema: list):
    """Insert df to BigQuery.

    Args:
        df (pd.DataFrame): Insert df.
        dataset_name (str): Dataset and Table names. Example: xxx-db.xxx-table
        project_id (str): GCP Project Id.
        table_schema (list): Schema of table to insert.

    Raises:
        InvalidSchema: Different from the schema of the table that df inserts.
    """
    try:
        df.to_gbq(
            dataset_name,
            project_id=project_id,
            if_exists="append",
            table_schema=table_schema
        )
    except pandas_gbq.gbq.InvalidSchema as InvalidSchema:
        # Make to "logging"
        """
        print("---df---")
        print(df)
        print("---table_schema---")
        print(table_schema)
        """
        raise InvalidSchema
