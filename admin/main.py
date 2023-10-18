import configparser
import os

from flask import Flask
from flask_mysqldb import MySQL

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
# Configuring Environment Variables
config = configparser.ConfigParser()
config.read(f'{BASE_DIR}/.env')
mysql = MySQL()

app.config['MYSQL_USER'] = config['local']['user']
app.config['MYSQL_PASSWORD'] = config['local']['password']
app.config['MYSQL_DB'] = config['local']['name']
app.config['MYSQL_HOST'] = config['local']['host']
app.config['MYSQL_PORT'] = int(config['local']['port'])
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql.init_app(app)


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
