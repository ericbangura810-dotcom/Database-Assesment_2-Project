from db import get_connection

def delivery_progress_by_status():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT status, COUNT(*) AS count
    FROM shipments
    GROUP BY status
    ORDER BY status;
    """)

    rows = cur.fetchall()
    conn.close()
    return rows