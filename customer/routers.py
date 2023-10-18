import json

from flask import Blueprint, jsonify
from flask_pydantic import validate
from flask_pyjwt import require_token
from flask_mail import Message
from werkzeug.security import check_password_hash

from serializers import CustomerLogin, CustomerToken, HireVehicle
from crud import retrieve_customer as r_customer, list_vehicles as l_vehicles, hire_vehicle as h_vehicle, \
    get_vehicle as g_vehicle, create_invoice as c_invoice, get_customer as g_customer
from main import auth_manager, app, mail

customer_route = Blueprint('customer_route', __name__, url_prefix='/customer')


@customer_route.route('/login/', methods=['POST'])
@validate()
def login(body: CustomerLogin):
    """
    Body Customer Create
    :param body: request data
    :return: user data & tokens with 201 status code
    """
    # data will be used to create a new user into the database
    email = body.email
    password = body.password
    user = r_customer(email=email)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({'message': 'user not found'}), 403
    # Create the auth and refresh tokens
    auth_token = auth_manager.auth_token(user['id'])
    refresh_token = auth_manager.refresh_token(user['id'])
    print(auth_token, refresh_token)
    resp = CustomerToken(**user, auth_token=auth_token.signed, refresh_token=refresh_token.signed)
    return resp, 201


item_route = Blueprint('item_route', __name__, url_prefix='/item')


@item_route.route('/list', methods=['GET'])
@require_token()
def list_vehicles():
    """
    Query Vehicles
    :return: list of vehicles
    """
    vehicles = l_vehicles()
    data = []
    for vehicle in vehicles:
        category = vehicle.pop('category')
        category = json.loads(category)
        data.append({**vehicle, "category": category})
    return data, 200


@item_route.route('/hire/', methods=['POST'])
@require_token()
def list_vehicles(body: HireVehicle):
    """
    Create Booking
    :param body: request data
    """
    vehicle_id = body.vehicle_id
    vehicle = g_vehicle(vehicle_id)
    if vehicle["available"]:
        booking = h_vehicle(**body.model_dump())
        invoice = c_invoice(booking['id'], body.amount)
        user = g_customer(body.customer_id)
        # send confirmation email
        msg = Message('Invoice', sender=app.config['MAIL_SERVER'], recipients=[user['email']], body=json.dumps(invoice))
        mail.send(msg)
        return body, 201
    return jsonify({'message': 'vehicle not available'}), 403
