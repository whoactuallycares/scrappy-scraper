import psycopg2


def db_connect():
    try:
        conn = psycopg2.connect("dbname='postgres' user='postgres' host='database' password='postgres'")
        return conn
    except psycopg2.OperationalError as err:
        print(f"Unable to connect to the database\n{err}")

def db_create_table(conn):
    cur = conn.cursor()
    cur.execute(f"""CREATE TABLE listings(id VARCHAR PRIMARY KEY, name VARCHAR, price VARCHAR, location VARCHAR, image_urls VARCHAR)""")

def db_destroy_table(conn):
    cur = conn.cursor()
    cur.execute(f"""DROP TABLE IF EXISTS listings""")

def db_insert(conn, id, name, price, location, image_urls):
    cur = conn.cursor()
    cur.execute(f"""INSERT INTO listings("id", "name", "price", "location", "image_urls") VALUES('{id}', '{name}', '{price}', '{location}', '{image_urls}')""")

def db_read(conn):
    cur = conn.cursor()
    cur.execute(f"""SELECT id,name,price,location,image_urls FROM listings""")
    return cur.fetchall()