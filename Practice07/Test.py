import psycopg2
from Connect import DB_host, DB_base, DB_user, DB_pass
conn = psycopg2.connect(
    host=DB_host,
    database=DB_base,
    user=DB_user,
    password=DB_pass
)


create_table_query = '''
        CREATE TABLE IF NOT EXISTS   (
            id SERIAL PRIMARY KEY,
            product_name VARCHAR(100) NOT NULL,
            brand VARCHAR(50),
            category VARCHAR(50),
            price NUMERIC(10, 2),
            stock_quantity INTEGER,
            is_available BOOLEAN DEFAULT TRUE,
            last_restock_date DATE
        );
        '''
insert_query = """ INSERT INTO inventory 
                           (product_name, brand, category, price, stock_quantity, is_available, last_restock_date) 
                           VALUES (%s, %s, %s, %s, %s, %s, %s) """
        
products_to_insert = [
    ('iPhone 15', 'Apple', 'Smartphone', 999.99, 15, True, '2026-03-01'),
    ('Galaxy S24', 'Samsung', 'Smartphone', 899.50, 0, False, '2026-02-15'),
    ('MacBook Air', 'Apple', 'Laptop', 1200.00, 8, True, '2026-03-10'),
    ('AirPods Pro', 'Apple', 'Headphones', 249.99, 20, True, '2026-03-15'),
    ('Logitech MX Master', 'Logitech', 'Accessories', 99.00, 10, True, '2026-02-20'),
    ('Kindle Paperwhite', 'Amazon', 'E-reader', 139.99, 0, False, '2026-01-10'),
    ('RTX 4080', 'NVIDIA', 'GPU', 1199.00, 3, True, '2026-03-25'),
    ('Monitor 27"', 'Dell', 'Monitor', 299.50, 12, True, '2026-03-28')
]

with conn.cursor() as cur:
    cur.execute(create_table_query)
    cur.executemany(insert_query, products_to_insert)
    conn.commit()

conn.close()