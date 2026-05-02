from datetime import datetime
from db import get_connection

def add_shipment(order_number, sender_name, sender_address_encrypted,
                 receiver_name, receiver_address_encrypted, item_description,
                 origin_warehouse_id, destination_warehouse_id,
                 expected_delivery_date):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
      INSERT INTO shipments (
      order_number, sender_name, sender_address_encrypted,
      receiver_name, receiver_address_encrypted, item_description,
      origin_warehouse_id, destination_warehouse_id,
      status, created_at, expected_delivery_date
      ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'in transit' , ?, ?)
      """, (
        order_number, sender_name, sender_address_encrypted,
        receiver_name, receiver_address_encrypted, item_description,
        origin_warehouse_id, destination_warehouse_id,
        datetime.now().isoformat(), expected_delivery_date
    ))

    conn.commit()
    shipment_id = cur.lastrowid
    conn.close()
    return shipment_id

def update_shipment_statuss(shipment_id, status):
    conn = get_connection()
    conn.execute("""
    UPDATE shipments
    SET status = ?
    WHERE id = ?
    """, (status, shipment_id))
    conn.commit()
    conn.close()

def get_shipment(shipment_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""SELECT * FROM shipments WHERE id = ?""", (shipment_id,))
    row = cur.fetchone()
    conn.close()
    return row







