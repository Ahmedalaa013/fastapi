from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from fastapi.params import Body

from routers import products,categories


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(products.router)
app.include_router(categories.router)


@app.get("/")
def home():
    return {"message": "Hello welcome to fast api"}


# @app.post('/post', status_code=status.HTTP_201_CREATED)
# def post(payload: Post):
#     cur.execute(""" insert into posts (title,content,published) values (%s,%s,%s) RETURNING * """,
#                 [payload.title, payload.content, payload.published])
#     new_post = cur.fetchone()
#     conn.commit()
#     return {"data": new_post}


