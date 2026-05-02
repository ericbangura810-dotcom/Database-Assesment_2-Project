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

def warehouses_activity_summary(warehouse_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT activity_type, COUNT(*) AS events, SUM(quantity_change) AS total_quantity_change
    FROM warehouse_activity_logs
    WHERE warehouse_id = ?
    GROUP BY activity_type
    ORDER BY activity_type;
    """, (warehouse_id,))

    rows = cur.fetchall()
    conn.close()
    return rows