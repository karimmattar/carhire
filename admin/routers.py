from flask import Blueprint, jsonify
from flask_pydantic import validate

from serializers import Customer, CustomerCreate, RetrieveCustomer
from crud import create_customer as c_customer, retrieve_customer as r_customer, update_customer as u_customer, \
    delete_customer as d_customer

customer_route = Blueprint('customer_route', __name__, url_prefix='/customer')


@customer_route.route('/create/', methods=['POST'])
@validate()
def create_customer(body: CustomerCreate):
    """
    Body Customer Create
    :param body: request data
    :return: user data with 201 status code
    """
    # data will be used to create a new user into the database
    data = body.model_dump()
    user = c_customer(**data)
    resp = RetrieveCustomer(**user)
    return resp, 201


@customer_route.route('/update/<int:uid>/', methods=['PUT', 'PATCH'])
@validate()
def update_customer(uid: int, body: Customer):
    """
    Body Customer Update
    :param uid: customer id
    :param body: request data
    :return: no content with 204 status code
    """
    # data will be used to update an existing user
    data = body.model_dump()
    u_customer(**data, uid=uid)
    return body, 204


@customer_route.route('/delete/<int:uid>/', methods=['DELETE'])
@validate()
def delete_customer(uid: int):
    """
    Customer Delete by id
    :param uid: user id
    :return: json with 200 status code
    """
    # delete users with given id
    d_customer(uid)
    return jsonify({'message': 'user deleted'}), 200


@customer_route.route('/<int:uid>', methods=['GET'])
@validate()
def retrieve_customer(uid: int):
    """
    Query Customer
    :param uid: user id
    :return: user data with 200 status code
    """
    user = r_customer(uid)
    if not user:
        return jsonify({'message': 'user not found'}), 404
    # fetch users with given id
    data = RetrieveCustomer(**user)
    return data.model_dump(), 200
