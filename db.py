import sqlite3

def get_db_conection():
    conn = sqlite3.connect('productos.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_conection()
    conn.execute('''
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        price REAL NOT NULL,
        image TEXT
    )
''')
    conn.commit()
    conn.close()

def get_all_products():
    conn = get_db_conection()
    products = conn.execute('SELECT * FROM products').fetchall()
    conn.close()
    return products

def add_product(name, description, price, image):
    conn = get_db_conection()
    conn.execute('INSERT INTO products (name, description, price, image) VALUES (?,?,?,?)', (name, description, price, image))
    conn.commit()
    conn.close()

def update_product(product_id, name, description, price, image):
    conn = get_db_conection()
    conn.execute('''
        UPDATE products 
        SET name = ?, description = ?, price = ?, image = ? 
        WHERE id = ?
    ''', (name, description, price, image, product_id))
    conn.commit()
    conn.close()


def delete_product(producto_id):
    conn = get_db_conection()
    conn.execute('DELETE FROM products WHERE id = ?', (producto_id,))
    conn.close()
    