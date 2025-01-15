from fastapi import APIRouter, HTTPException
from business.table1_business import DatabaseService  # Import your DatabaseService class
from pydantic import BaseModel

router = APIRouter()
db_service = DatabaseService()

# class RecordCreate(BaseModel):
#     c_text: str
#     c_double: float

# create table route
@router.post("/create/")
async def create_table1_record():
    record_id = db_service.create_record()
    return {"id": record_id, "message": "Record created successfully"}

@router.get("/get_all/")
async def get_all_table1_records():
    """
    Retrieve all records from Table1.

    Returns:
        List[Table1Response]: A list of all records.
    """
    return db_service.read_records()


