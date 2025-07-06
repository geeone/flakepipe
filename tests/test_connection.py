from unittest.mock import patch, MagicMock

from flakepipe.connection import get_engine


@patch("flakepipe.connection.create_engine")
@patch("flakepipe.connection.URL")
def test_get_engine_basic(mock_url, mock_create_engine):
    # Arrange
    config = {
        'SF_USER': 'test_user',
        'SF_PASSWORD': 'test_pass',
        'SF_ACCOUNT': 'test_account',
        'SF_ROLE': 'SYSADMIN',
        'SF_DATABASE': 'TEST_DB',
        'SF_WAREHOUSE': 'COMPUTE_WH'
    }
    schema = 'PUBLIC'
    mock_url.return_value = "mocked_url"
    mock_engine = MagicMock()
    mock_create_engine.return_value = mock_engine

    # Act
    engine = get_engine(config, schema)

    # Assert
    mock_url.assert_called_once_with(
        user='test_user',
        password='test_pass',
        account='test_account',
        role='SYSADMIN',
        database='TEST_DB',
        schema='PUBLIC',
        warehouse='COMPUTE_WH'
    )
    mock_create_engine.assert_called_once_with("mocked_url")
    assert engine == mock_engine


@patch("flakepipe.connection.create_engine")
@patch("flakepipe.connection.URL")
def test_get_engine_with_keep_alive(mock_url, mock_create_engine):
    config = {
        'SF_USER': 'user',
        'SF_PASSWORD': 'pass',
        'SF_ACCOUNT': 'account',
        'SF_ROLE': 'role',
        'SF_DATABASE': 'db',
        'SF_WAREHOUSE': 'wh'
    }
    schema = 'myschema'
    mock_url.return_value = "url"
    mock_engine = MagicMock()
    mock_create_engine.return_value = mock_engine

    engine = get_engine(config, schema, keep_alive=True)

    mock_create_engine.assert_called_once_with(
        "url",
        connect_args={'client_session_keep_alive': True}
    )
    assert engine == mock_engine
