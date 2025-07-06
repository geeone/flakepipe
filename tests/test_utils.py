from unittest.mock import MagicMock, patch

from flakepipe.utils import normalize_columns, check_if_exists
import pandas as pd


def test_normalize_columns():
    input_columns = ["Name", "age", "e-mail",
                     "some column", "weird___column!!"]
    expected = ["NAME", "AGE", "E_MAIL", "SOME_COLUMN", "WEIRD_COLUMN_"]
    result = normalize_columns(input_columns)
    assert result == expected


@patch("flakepipe.utils.pd.read_sql")
def test_check_if_exists_true(mock_read_sql):
    mock_read_sql.return_value = pd.DataFrame({"name": ["MYTABLE"]})
    engine = MagicMock()
    schema = "MYSCHEMA"
    table = "MYTABLE"

    result = check_if_exists(engine, schema, table)

    mock_read_sql.assert_called_once()
    assert result is True


@patch("flakepipe.utils.pd.read_sql")
def test_check_if_exists_false(mock_read_sql):
    mock_read_sql.return_value = pd.DataFrame(columns=["name"])
    engine = MagicMock()
    schema = "MYSCHEMA"
    table = "MISSING_TABLE"

    result = check_if_exists(engine, schema, table)

    mock_read_sql.assert_called_once()
    assert result is False
