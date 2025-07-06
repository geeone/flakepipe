from unittest.mock import patch, MagicMock

from flakepipe import uploader
import pandas as pd


@patch("flakepipe.uploader.os.remove")
@patch("flakepipe.uploader.pd.read_sql")
@patch("flakepipe.uploader.create_table")
@patch("flakepipe.uploader.pd.read_csv")
@patch("flakepipe.uploader.normalize_columns")
@patch("flakepipe.uploader.check_if_exists")
@patch("flakepipe.uploader.get_engine")
def test_upload_csv_creates_and_uploads(
    mock_get_engine, mock_check_exists, mock_normalize,
    mock_read_csv, mock_create_table, mock_read_sql, mock_remove
):
    # Arrange
    config = {
        'SF_USER': 'user',
        'SF_PASSWORD': 'pass',
        'SF_ACCOUNT': 'acc',
        'SF_ROLE': 'role',
        'SF_DATABASE': 'db',
        'SF_WAREHOUSE': 'wh'
    }
    engine = MagicMock()
    mock_get_engine.return_value = engine
    mock_check_exists.return_value = False

    df = pd.DataFrame({"Name": ["Alice"], "Age": ["30"]})
    mock_read_csv.return_value = df
    mock_normalize.return_value = ["NAME", "AGE"]

    # Act
    uploader.upload_csv_to_snowflake(
        config=config,
        file_path="data.csv",
        schema="MYSCHEMA",
        table_name="users",
        truncate=False,
        overwrite=False,
        prefix="daily",
        postfix="20250706"
    )

    # Assert
    expected_table = "DAILY_USERS_20250706"
    mock_create_table.assert_called_once_with(
        engine, expected_table, ["NAME", "AGE"], False)
    assert mock_read_sql.call_count == 2
    engine.dispose.assert_called_once()
    mock_remove.assert_called_once_with("data.csv")


@patch("flakepipe.uploader.truncate_table")
@patch("flakepipe.uploader.os.remove")
@patch("flakepipe.uploader.pd.read_sql")
@patch("flakepipe.uploader.create_table")
@patch("flakepipe.uploader.pd.read_csv")
@patch("flakepipe.uploader.normalize_columns")
@patch("flakepipe.uploader.check_if_exists")
@patch("flakepipe.uploader.get_engine")
def test_upload_csv_with_truncate(
    mock_get_engine, mock_check_exists, mock_normalize,
    mock_read_csv, mock_create_table, mock_read_sql,
    mock_remove, mock_truncate
):
    config = {k: "val" for k in [
        'SF_USER', 'SF_PASSWORD', 'SF_ACCOUNT', 'SF_ROLE',
        'SF_DATABASE', 'SF_WAREHOUSE']}
    engine = MagicMock()
    mock_get_engine.return_value = engine
    mock_check_exists.return_value = True
    df = pd.DataFrame({"x": [1]})
    mock_read_csv.return_value = df
    mock_normalize.return_value = ["X"]

    uploader.upload_csv_to_snowflake(
        config=config,
        file_path="data.csv",
        schema="SCH",
        table_name="t1",
        truncate=True,
        overwrite=False
    )

    mock_truncate.assert_called_once()
