import pytest
from unittest.mock import patch
from src.main import extract_bq, get_secret
import pandas as pd


def test_extract_bsgq():
    assert 3 == 3


@patch("src.main.secretmanager.SecretManagerServiceClient.access_secret_version")
def test_get_secret(secretmanager):
    secretmanager.return_value.payload.data = b'super_secret_token'
    secret_string = get_secret('project_id', 'secret_name')

    assert secret_string == 'super_secret_token'


@patch("src.main.bigquery.Client.query", return_value="True")
def test_extract_bq(mock_bigquery):


    result_df = extract_bq("query")
    print("あsdf亜sdf亞sdfあsdf亜sdf亜sdf亜sdf亞sdf亜sdf亜sdf亜sdf亜sdf亜sdfあ")
    print(result_df)
    print("あsdf亜sdf亞sdfあsdf亜sdf亜sdf亜sdf亞sdf亜sdf亜sdf亜sdf亜sdf亜sdfあ")
    aa = "aaa"

    assert result_df == aa

# BigQueryのtestではなくdfを返す関数のtestとして再調査
