from fastapi import FastAPI
from routers import drug


app = FastAPI()

app.include_router(drug.router, prefix="/drugs", tags=["Drugs"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Drug API"}

@app.get("/ping")
def ping():
    return {"message": "pong"}
