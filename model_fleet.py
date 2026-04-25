from datetime import datetime
from db import get_connection

def assign_driver_to_shipment(shipment_id, driver_id, vehicle_id, route_details):
    conn = get_connection()
    cur = conn.cursor()

    assigned_at = datetime.now().isoformat()

    cur.execute("""
    INSERT INTO delivery_records (
    shipment_id, driver_id, vehicle_id, route_details, assigned_at, current_status )
    VALUES (?, ?, ?, ?, ?, 'in_transit') """, (shipment_id, driver_id, vehicle_id, route_details, assigned_at))

    cur.execute("""
        UPDATE vehicles
        SET status = 'in_use'
        WHERE id = ? 
    """, (vehicle_id,))
