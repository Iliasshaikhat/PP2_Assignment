import psycopg2
from Config import DB_CONFIG

def get_connection():
    return psycopg2.connect(**DB_CONFIG)