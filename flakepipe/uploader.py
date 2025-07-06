import os

import pandas as pd

from .connection import get_engine
from .utils import check_if_exists, normalize_columns


def create_table(engine, table_name, columns, overwrite=False):
    replace_clause = "OR REPLACE" if overwrite else ""
    column_defs = ", ".join(f"{col} TEXT" for col in columns)
    sql = f"CREATE {replace_clause} TABLE {table_name} ({column_defs})"
    with engine.connect() as conn:
        conn.execute(sql)


def truncate_table(engine, table_name):
    sql = f"TRUNCATE TABLE {table_name}"
    with engine.connect() as conn:
        conn.execute(sql)


def upload_csv_to_snowflake(config, file_path, schema, table_name,
                            truncate=False, overwrite=False,
                            prefix=None, postfix=None):
    engine = get_engine(config, schema, keep_alive=True)
    try:
        if prefix:
            table_name = f"{prefix}_{table_name}"
        if postfix:
            table_name = f"{table_name}_{postfix}"

        table_name = table_name.upper()

        if not check_if_exists(engine, schema, table_name) or overwrite:
            df = pd.read_csv(file_path, dtype=object)
            df.columns = normalize_columns(df.columns)
            df.to_csv(file_path, index=False, quoting=1, encoding='utf-8')
            create_table(engine, table_name, df.columns.to_list(), overwrite)

        if truncate and not overwrite:
            truncate_table(engine, table_name)

        put_sql = f"PUT file://{file_path} @temp_stage OVERWRITE = TRUE"
        pd.read_sql(put_sql, engine)

        filename = os.path.basename(file_path)
        copy_sql = f"""
            COPY INTO {table_name}
            FROM '@temp_stage/{filename}'
            FILE_FORMAT=(field_optionally_enclosed_by='"' skip_header=1 NULL_IF='')
            ON_ERROR='SKIP_FILE'
        """
        pd.read_sql(copy_sql, engine)
    finally:
        engine.dispose()
        os.remove(file_path)
