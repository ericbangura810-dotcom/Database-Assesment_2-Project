from datetime import datetime
from db import get_connection


def adjust_inventory(warehouse_id, item_id, quantity_change, activity_type, related_shipment_id = None, performed_by_user_id = None):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT OR IGNORE INTO warehous_inventory (warehouse_id, item_id, quantity)
                VALUES (?, ?, 0)
                """, (warehouse_id, item_id))

    cur.execute("""
    UPDATE warehous_inventory 
    SET quantity = quantity + ?
    WHERE warehouse_id = ? AND item_id = ?
    """, (quantity_change, warehouse_id, item_id))

    cur.execute("""
    INSERT INTO warehoue_activity_logs (warehouse_id, activity_type, item_id, quantity_change, related_shipment_id, timestamp, performed_by_user_id)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """,(warehouse_id, activity_type, item_id, quantity_change, related_shipment_id, datetime.now(), performed_by_user_id))

    conn.commit()
    conn.close()



