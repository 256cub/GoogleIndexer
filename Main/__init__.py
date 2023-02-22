import os
from urllib.parse import urlparse
from colorama import Fore, Style, Back

import mysql.connector
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env file

DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_DATABASE = os.environ.get('DB_DATABASE')
SITEMAP_URL = os.environ.get('SITEMAP_URL')

DEFAULT_STATUS = 'ACTIVE'

# Get the absolute path of the current file (the script that is running)
current_file_path = os.path.abspath(__file__)

# Get the directory name of the current file (i.e. the parent directory of the script)
current_dir = os.path.dirname(current_file_path)

# Get the absolute path of the current app (i.e. the parent directory of the parent directory of the script)
APP_PATH = os.path.dirname(current_dir) + '/'


class MySQL:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=os.environ.get('DB_HOST'),
            user=os.environ.get('DB_USER'),
            passwd=os.environ.get('DB_PASSWORD'),
            database=os.environ.get('DB_DATABASE'),
            auth_plugin="mysql_native_password"
        )

    def select(self, query):
        sql_cursor = self.connection.cursor(dictionary=True)
        sql_cursor.execute(query)
        sql_result = sql_cursor.fetchall()
        sql_cursor.close()
        return sql_result

    def select_single(self, query):
        sql_cursor = self.connection.cursor(dictionary=True)
        sql_cursor.execute(query)
        sql_result = sql_cursor.fetchone()
        sql_cursor.close()
        return sql_result

    def update(self, query):
        sql_cursor = self.connection.cursor()
        sql_cursor.execute(query)
        self.connection.commit()
        last_row = sql_cursor.fetchone()
        sql_cursor.close()
        return last_row

    def insert(self, query):
        sql_cursor = self.connection.cursor()
        sql_cursor.execute(query)
        self.connection.commit()
        last_row_id = sql_cursor.lastrowid
        sql_cursor.close()
        return last_row_id

    def close(self):
        self.connection.close()


def get_websites(website_id=False, status=DEFAULT_STATUS, limit=False):
    try:

        if website_id:
            query = "SELECT * FROM `websites` WHERE `id` = {}".format(website_id)
            return MySQL().select_single(query)

        query = "SELECT * FROM `websites` WHERE `status` = '{}'".format(status)

        if limit:
            query += " LIMIT '{}'".format(limit)

        return MySQL().select(query)
    except Exception as exception:
        print(exception)


def get_urls(website_id=False, status=DEFAULT_STATUS, limit=False):
    try:

        query = "SELECT * FROM `urls` WHERE `status` = '{}'".format(status)

        if website_id:
            query += " AND `websites_id` = {}".format(website_id)

        if limit:
            query += " LIMIT '{}'".format(limit)

        return MySQL().select(query)
    except Exception as exception:
        print(exception)


def get_hostname_from_url(url):
    # Parse the URL using urlparse
    parsed_url = urlparse(url)

    # return the hostname from the parsed URL
    return parsed_url.hostname


def save_url(url):
    try:

        query = "SELECT * FROM `urls` WHERE `status` = '{}'".format(status)

        if website_id:
            query += " AND `websites_id` = {}".format(website_id)

        if limit:
            query += " LIMIT '{}'".format(limit)

        return MySQL().select(query)
    except Exception as exception:
        print(exception)


def check_if_row_exist(table, column_name, column_value):
    try:
        query = "SELECT * FROM `{}` WHERE `{}` = \"{}\"".format(table, column_name, column_value)

        result = MySQL().select_single(query)
        if result:
            return result['id']

        return False
    except Exception as exception:
        print(exception)


def insert_row_into_table(table, columns):
    try:
        query = "INSERT INTO `{}` ".format(table)

        columns_name = []
        columns_value = []
        for column_name in columns:
            columns_name.append('`' + column_name + '`')
            if columns[column_name] is None:
                columns_value.append('0')
            else:
                columns_value.append('"' + str(columns[column_name]) + '"')

        query += " ({}) VALUES ({}) ".format(', '.join(columns_name), ', '.join(columns_value))

        return MySQL().insert(query)
    except Exception as exception:
        print(exception)
