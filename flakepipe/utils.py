
import pandas as pd
import re

def normalize_columns(columns):
    return [re.sub(r'_+', '_', re.sub(r'[^a-zA-Z\d]', '_', col)).upper() for col in columns]

def check_if_exists(engine, schema, table_name):
    result = pd.read_sql(
        f"""
        SELECT table_name AS name FROM information_schema.tables
        WHERE table_name='{table_name}' AND table_schema='{schema}'
        """, engine)
    return not result.empty
