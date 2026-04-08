import psycopg2
from Connect import DB_host, DB_base, DB_user, DB_pass
conn = psycopg2.connect(
    host=DB_host,
    database=DB_base,
    user=DB_user,
    password=DB_pass
)

inser_func = "SELECT * FROM inventory WHERE product_name LIKE '%Pro%' "

with conn.cursor() as cur:
    cur.execute(inser_func)
    for i in cur.fetchall() :
        print(i)
    conn.commit()

conn.close()