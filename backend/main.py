from fastapi import FastAPI
from routers import users
from routers import stocks
from routers import getondemand
app = FastAPI()

app.include_router(users.router, prefix="/user")
app.include_router(stocks.router, prefix= "/stocks")
app.include_router(getondemand.router, prefix="/getondemand")
@app.get("/")
async def root():
    return {"message": "Root Node"}
 
