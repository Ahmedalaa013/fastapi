import psycopg2
from psycopg2.extras import RealDictCursor



def open_connection():
    conn = psycopg2.connect(host='localhost', database='fastapi',
                                user='postgres', password='admin', cursor_factory=RealDictCursor)
    return conn


def db_get_all(query):
    try:
        conn = open_connection()
        cur =conn.cursor() 
        cur.execute(query)
        rows = cur.fetchall()
        conn.close()
        return rows      
    except Exception as error:
        print('Connection to db failed')
        print('Error:',error)

def db_get_single(query):
    try:
        conn = open_connection()
        cur =conn.cursor()  
        cur.execute(query)
        rows = cur.fetchone()
        conn.close()
        return rows      
    except Exception as error:
        print('Connection to db failed')
        print('Error:',error)

def db_create_product(query):
    try:
        conn = open_connection()
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        products = cur.fetchall()
        conn.close()
        return products
    except Exception as error:
        return error
