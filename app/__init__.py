"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-ch12tf8rddl13a53hvpg-a.oregon-postgres.render.com",
        database="todo_0tzt",
        user="root",
        password="49995SPp1CEXGWSVoDBlySpM6ftVkSzq")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
