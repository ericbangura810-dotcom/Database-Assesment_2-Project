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

    def require_role(self, role):
        if not user_has_role(self.user, role):
            raise Exception(f"User does not have required role: {role}")

    def create_shipment(self, **kwargs):
        if not (user_has_role(self.user, "manager") or user_has_role(self.user, "admin")):
            raise Exception("Only managers or admins can create shipments.")








