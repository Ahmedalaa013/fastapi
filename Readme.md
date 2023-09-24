# Fast API CRUD Task


## Requirements

1. python to be installed on your machine
2. pip package manager to be installed on your machine
3. creata a postgresql database named fastapi
4. create category table with column names (id,name)
5. create products table with column names (id,p_name,price,quantity,imageurl,category_id)
6. make sure category_id is forign key that references the id column in category table
7. populate the tables with some data



### Getting started

1. run pip install -r requirements.txt
2. from inside the app directory open a terminal window and run uvicorn main:app --reload
3. in app/src/db.py file add your postgresql database credentials (host,user,password) in open_connection function
4. open postman and start using the api collection
