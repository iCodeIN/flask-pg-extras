from flask_pg_extras import db_execute_results


def query(db):
    q = """
    SELECT
      'index hit rate' AS name,
      (sum(idx_blks_hit)) / nullif(sum(idx_blks_hit + idx_blks_read),0) AS ratio
    FROM pg_statio_user_indexes
    UNION ALL
    SELECT
     'table hit rate' AS name,
      sum(heap_blks_hit) / nullif(sum(heap_blks_hit) + sum(heap_blks_read),0) AS ratio
    FROM pg_statio_user_tables;
    """

    return db_execute_results(db, q)
