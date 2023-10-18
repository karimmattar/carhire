from main import db_connection, db_commit, db_close


def retrieve_customer(email):
    """
    Query Customer
    :param email: customer email
    :return: row sql as dict
    """
    cursor = db_connection()
    query = f"SELECT * FROM customer WHERE email = '{email}'"
    cursor.execute(query)
    user = cursor.fetchone()
    db_close(cursor)
    return user


def get_customer(uid):
    """
    Query Customer
    :param uid: customer id
    :return: row sql as dict
    """
    cursor = db_connection()
    query = f"SELECT * FROM customer WHERE id = {uid}"
    cursor.execute(query)
    user = cursor.fetchone()
    db_close(cursor)
    return user


def list_vehicles():
    """
    Query Vehicles
    :return: list of vehicles
    """
    cursor = db_connection()
    query = "SELECT v.id, v.description, v.color, v.brand, v.model, JSON_OBJECT('id', vc.id, 'name', vc.name, 'max_capacity', vc.max_capacity) As category FROM vehicle v JOIN vehicle_category vc on vc.id = v.category_id"
    cursor.execute(query)
    vehicles = cursor.fetchall()
    db_close(cursor)
    return vehicles


def get_vehicle(uid):
    """
    Query Vehicle
    :param uid: vehicle id
    :return: vehicle sql as dict
    """
    cursor = db_connection()
    query = f"SELECT * FROM vehicle WHERE id = {uid}"
    cursor.execute(query)
    vehicle = cursor.fetchone()
    db_close(cursor)
    return vehicle


def hire_vehicle(customer_id, vehicle_id, pickup_date, return_date, amount):
    """
    Create Booking
    :param customer_id: customer id
    :param vehicle_id: vehicle id
    :param pickup_date: pickup date
    :param return_date: return date
    :param amount: amount
    :return: booking id
    """
    cursor = db_connection()
    query = f"INSERT INTO booking(customer_id, vehicle_id, pickup_date, return_date, amount) VALUES({customer_id}, {vehicle_id}, '{pickup_date}', '{return_date}', {amount})"
    cursor.execute(query)
    db_commit()
    # Update user status to pending
    query = f"UPDATE customer SET status = 'pending' WHERE id = {customer_id}"
    cursor.execute(query)
    db_commit()
    # Set that car not more available
    query = f"UPDATE vehicle SET available = false WHERE id = {vehicle_id}"
    cursor.execute(query)
    db_commit()
    query = f"SELECT id FROM booking WHERE customer_id = {customer_id}, vehicle_id = {vehicle_id}, pickup_date = '{pickup_date}', return_date = '{return_date}'"
    cursor.execute(query)
    booking = cursor.fetchall()[-1]
    db_close(cursor)
    return booking


def create_invoice(booking_id, amount):
    """
    Create Invoice
    :param booking_id: booking id
    :param amount: amount
    :return: invoice id
    """
    cursor = db_connection()
    query = f"INSERT INTO invoice(booking_id, amount) VALUES({booking_id}, {amount})"
    cursor.execute(query)
    db_commit()
    # return invoice id
    query = f"SELECT id FROM invoice WHERE booking_id = {booking_id}"
    cursor.execute(query)
    invoice = cursor.fetchall()[-1]
    db_close(cursor)
    return invoice
