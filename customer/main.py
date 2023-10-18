import configparser
import os

from flask import Flask
from flask_mysqldb import MySQL
from flask_pyjwt import AuthManager
from flask_mail import Mail

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
# Configuring Environment Variables
config = configparser.ConfigParser()
config.read(f'{BASE_DIR}/.env')
# database configuration
app.config['MYSQL_USER'] = config['local']['user']
app.config['MYSQL_PASSWORD'] = config['local']['password']
app.config['MYSQL_DB'] = config['local']['name']
app.config['MYSQL_HOST'] = config['local']['host']
app.config['MYSQL_PORT'] = int(config['local']['port'])
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
# JWT configuration
app.config["JWT_ISSUER"] = "Flask_PyJWT"
app.config["JWT_AUTHTYPE"] = "HS256"
app.config["JWT_SECRET"] = "SECRETKEY"
app.config["JWT_AUTHMAXAGE"] = 3600
app.config["JWT_REFRESHMAXAGE"] = 604800
auth_manager = AuthManager(app)
# Mail configuration
app.config['MAIL_SERVER'] = config['local']['ehost']
app.config['MAIL_PORT'] = int(config['local']['eport'])
app.config['MAIL_USERNAME'] = config['local']['euser']
app.config['MAIL_PASSWORD'] = config['local']['epassword']
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


def db_connection():
    """
    DB Connection
    :return: db cursor
    """
    try:
        cursor = mysql.connection.cursor()
    except Exception as error:
        raise error
    return cursor


def db_close(cursor):
    """
    DB Close
    :param cursor: db cursor
    """
    try:
        cursor.close()
    except Exception as error:
        raise error


def db_commit():
    """
    DB Commit
    """
    try:
        mysql.connection.commit()
    except Exception as error:
        raise error
