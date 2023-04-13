"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrqa9hmbg5e4khrio30-a",
        database="todo_ykff",
        user="root",
        password="h8AW0lv7MGuW9iuMOn1m9Q82nDlXrHv7")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
