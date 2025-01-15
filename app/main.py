from fastapi import FastAPI
from service.service import router as table1_router

app = FastAPI()

# รวม router ของ Table1
app.include_router(table1_router, prefix="/table1", tags=["Table1"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}
