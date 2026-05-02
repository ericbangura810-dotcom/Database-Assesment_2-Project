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

        return add_shipment(**kwargs)

    def change_shipment_status(self, shipment_id, new_status):
        if not (user_has_role(self.user, "manager") or user_has_role(self.user, "admin")):
            raise Exception("Only managers or admins can update shipment status.")


        update_shipment_status(shipment_id, new_status)

    def view_shipment(self, shipment_id):
        if not (
                user_has_role(self.user, "warehouse")
                or user_has_role(self.user, "manager")
                or user_has_role(self.user, "admin")
        ):
            raise Exception("You do not have permission to view shipments.")

        return get_shipment(shipment_id)

    def assign_driver(self, shipment_id, driver_id, vehicle_id, route_details):
        if not (user_has_role(self.user, "manager") or user_has_role(self.user, "admin")):
            raise Exception("Only managers or admins can assign drivers.")

        assign_driver_to_shipment(shipment_id, driver_id, vehicle_id, route_details)

    def update_inventory(self, warehouse_id, item_id, quantity_change,
                         activity_type, related_shipment_id=None):

        if not (
                user_has_role(self.user, "warehouse")
                or user_has_role(self.user, "manager")
                or user_has_role(self.user, "admin")
        ):
            raise Exception("You do not have permission to update inventory.")

        adjust_inventory(
            warehouse_id,
            item_id,
            quantity_change,
            activity_type,
            related_shipment_id,
            performed_by_user_id=self.user["id"]
        )

    def report_delivery_progress(self):
        if not (user_has_role(self.user, "manager") or user_has_role(self.user, "admin")):
            raise Exception("Only managers or admins can view reports.")

        return delivery_progress_by_status()