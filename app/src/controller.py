from .db import db_get_all,db_get_single,db_create_product


def get_all_items(table_name,filter=""):
    if filter:
        query =f"select * from {table_name} where category_id = {filter}"
    else:
        query = f"select * from {table_name}"
    rows = db_get_all(query)
    return rows


def get_latest_product():
    query = "select * from products"
    rows = db_get_all(query)
    latest = rows[-1]
    return latest


def get_single_product(id):
    query = f"select * from products where id={id}"
    rows = db_get_single(query)
    return rows

def create_product(payload):
    query = """
    INSERT INTO products (p_name,price,quantity,imageURL,category_id) values ('{0}',{1},{2},'{3}',{4}) RETURNING * """.format(payload.p_name,payload.price,payload.quantity,payload.imageurl,payload.category_id)
    print(query)
    product = db_create_product(query)
    return product
