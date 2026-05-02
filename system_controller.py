from security import user_has_role
from model_shipment import (
add_shipment, update_shipment_status, get_shipment
)
from models_inventory import adjust_inventory
from model_fleet import assign_driver_to_shipment
from reports import (
delivery_progress_by_status,
warehouses_activity_summary,
vehicle_utilisation
)

class NorthshoreSystem:
    def __init__(self, user):
        self.user = user






