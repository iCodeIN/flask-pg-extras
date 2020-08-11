from flask_pg_extras import db_execute_results


def query(db):
    q = """
    SELECT c.relname AS name,
      pg_size_pretty(pg_table_size(c.oid)) AS size
    FROM pg_class c
    LEFT JOIN pg_namespace n ON (n.oid = c.relnamespace)
    WHERE n.nspname NOT IN ('pg_catalog', 'information_schema')
    AND n.nspname !~ '^pg_toast'
    AND c.relkind IN ('r', 'm')
    ORDER BY pg_table_size(c.oid) DESC;
    """

    return db_execute_results(db, q)
