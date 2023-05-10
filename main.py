from schema import User

# here we imported the fastapi clas from fastapi library
from fastapi import FastAPI

# here we initiating fastapi
app = FastAPI()

# we use the app decorator that we we created to create route and define a function of what should happen in the route
@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/send_data/")
async def send_data(request : User):
    return request