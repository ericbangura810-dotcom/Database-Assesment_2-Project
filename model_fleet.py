from datetime import datetime
from db import get_connection

def assign_driver_to_shipment(shipment_id, driver_id, vehicle_id, route_details):
    conn = get_connection()
    cur = conn.cursor()
