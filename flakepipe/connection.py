
import snowflake.connector
from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine

def get_engine(config, schema, keep_alive=False):
    conn_url = URL(
        user=config['SF_USER'],
        password=config['SF_PASSWORD'],
        account=config['SF_ACCOUNT'],
        role=config['SF_ROLE'],
        database=config['SF_DATABASE'],
        schema=schema,
        warehouse=config['SF_WAREHOUSE']
    )
    kwargs = {
        'connect_args': {'client_session_keep_alive': keep_alive}
    } if keep_alive else {}
    return create_engine(conn_url, **kwargs)
