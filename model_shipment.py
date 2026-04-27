from datetime import datetime
from db import get_connection

def add_shipment(order_number, sender_name, sender_address_encrypted,
                 receiver_name, receiver_address_encrypted, item_description,
                 origin_warehouse, destination_warehouse_id,
                 expected_delivery_date):

    conn = get_connection()
    cur = conn.cursor()
