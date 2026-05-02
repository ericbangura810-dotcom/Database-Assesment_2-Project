from security import authenticate, encrypt_text
from system_controller import NorthshoreSystem



def login_screen():
    print("=== Northshore Logistics System ===")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    user = authenticate(username, password)
    if user:
        print(f"\nWelcome, {user['username']} ({user['role']})")
        return user
    else:
        print("\nInvalid username or password.")
        return None


def main_menu(system):
    while True:
        print("\n--- Main Menu ---")
        print("1. Create Shipment")
        print("2. Update Shipment Status")
        print("3. Assign Driver to Shipment")
        print("4. Update Inventory")
        print("5. Delivery Progress Report")
        print("6. Warehouse Activity Report")
        print("7. Vehicle Utilisation Report")
        print("8. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            create_shipment_cli(system)
        elif choice == "2":
            update_shipment_status_cli(system)
        elif choice == "3":
            assign_driver_cli(system)
        elif choice == "4":
            update_inventory_cli(system)
        elif choice == "5":
            show_delivery_progress(system)
        elif choice == "6":
            show_warehouse_activity(system)
        elif choice == "7":
            show_vehicle_utilisation(system)
        elif choice == "8":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")


def create_shipment_cli(system):
    print("\n--- Create Shipment ---")
    order_number = input("Order number: ")
    sender_name = input("Sender name: ")
    sender_address = encrypt_text(input("Sender address: "))
    receiver_name = input("Receiver name: ")
    receiver_address = encrypt_text(input("Receiver address: "))
    item_description = input("Item description: ")
    origin = int(input("Origin warehouse ID: "))
    destination = int(input("Destination warehouse ID: "))
    expected_date = input("Expected delivery date (YYYY-MM-DD): ")

    try:
        shipment_id = system.create_shipment(
            order_number=order_number,
            sender_name=sender_name,
            sender_address_enc=sender_address,
            receiver_name=receiver_name,
            receiver_address_enc=receiver_address,
            item_description=item_description,
            origin_warehouse_id=origin,
            destination_warehouse_id=destination,
            expected_delivery_date=expected_date
        )
        print(f"Shipment created with ID {shipment_id}")
    except Exception as e:
        print("Error:", e)


def update_shipment_status_cli(system):
    print("\n--- Update Shipment Status ---")
    shipment_id = int(input("Shipment ID: "))
    new_status = input("New status (in_transit/delivered/delayed/returned): ")

    try:
        system.change_shipment_status(shipment_id, new_status)
        print("Shipment status updated.")
    except Exception as e:
        print("Error:", e)


def assign_driver_cli(system):
    print("\n--- Assign Driver ---")
    shipment_id = int(input("Shipment ID: "))
    driver_id = int(input("Driver ID: "))
    vehicle_id = int(input("Vehicle ID: "))
    route_details = input("Route details: ")

    try:
        system.assign_driver(shipment_id, driver_id, vehicle_id, route_details)
        print("Driver assigned.")
    except Exception as e:
        print("Error:", e)


def update_inventory_cli(system):
    print("\n--- Update Inventory ---")
    warehouse_id = int(input("Warehouse ID: "))
    item_id = int(input("Item ID: "))
    qty = int(input("Quantity change (+/-): "))
    activity_type = input("Activity type (restock/outbound/inbound/transfer): ")

    try:
        system.update_inventory(warehouse_id, item_id, qty, activity_type)
        print("Inventory updated.")
    except Exception as e:
        print("Error:", e)


def show_delivery_progress(system):
    print("\n--- Delivery Progress Report ---")
    try:
        rows = system.report_delivery_progress()
        for r in rows:
            print(f"{r['status']}: {r['count']}")
    except Exception as e:
        print("Error:", e)


def show_warehouse_activity(system):
    print("\n--- Warehouse Activity Report ---")
    warehouse_id = int(input("Warehouse ID: "))

    try:
        rows = system.report_warehouse_activity(warehouse_id)
        for r in rows:
            print(f"{r['activity_type']}: {r['events']} events, qty change {r['total_quantity_change']}")
    except Exception as e:
        print("Error:", e)


def show_vehicle_utilisation(system):
    print("\n--- Vehicle Utilisation Report ---")
    try:
        rows = system.report_vehicle_utilisation()
        for r in rows:
            print(f"{r['registration_number']} | Status: {r['status']} | Trips: {r['trips']}")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    user = None
    while user is None:
        user = login_screen()

    system = NorthshoreSystem(user)
    main_menu(system)
