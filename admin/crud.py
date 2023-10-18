from main import db_close, db_connection, db_commit


def create_customer(ssn, first_name, last_name, email, mobile_phone, status, country, password):
    """
    Create a new customer
    :param password: customer password
    :param ssn: social society number
    :param first_name: first name
    :param last_name: last name
    :param email: email address
    :param mobile_phone: mobile number
    :param status: hiring status
    :param country: country
    """
    cursor = db_connection()
    query = f"INSERT INTO customer (ssn, first_name, last_name, email, mobile_phone, status, country, password) VALUES ('{ssn}', '{first_name}', '{last_name}', '{email}', '{mobile_phone}', '{status}', '{country}', '{password}')"
    cursor.execute(query)
    db_commit()
    query = f"SELECT * FROM customer WHERE email = '{email}'"
    cursor.execute(query)
    user = cursor.fetchone()
    db_close(cursor)
    return user


def update_customer(ssn, first_name, last_name, email, mobile_phone, status, country, uid):
    """
    Update an existing customer
    :param uid: customer id
    :param ssn: social society number
    :param first_name: first name
    :param last_name: last name
    :param email: email address
    :param mobile_phone: mobile number
    :param status: hiring status
    :param country: country
    """
    cursor = db_connection()
    query = f"UPDATE customer SET ssn = '{ssn}', first_name = '{first_name}', last_name = '{last_name}', email = '{email}', mobile_phone = '{mobile_phone}', status = '{status}', country = '{country}' WHERE id = {uid}"
    cursor.execute(query)
    db_commit()
    db_close(cursor)


def delete_customer(uid):
    """
    Delete an existing customer
    :param uid: customer id
    """
    cursor = db_connection()
    query = f"DELETE FROM customer WHERE id = {uid}"
    cursor.execute(query)
    db_commit()
    db_close(cursor)


def retrieve_customer(uid):
    """
    Query Customer
    :param uid: customer id
    :return:
    """
    cursor = db_connection()
    query = f"SELECT * FROM customer WHERE id = {uid}"
    cursor.execute(query)
    user = cursor.fetchone()
    db_close(cursor)
    return user
