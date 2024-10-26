from fastapi import APIRouter
from datetime import date, datetime
from supabase import create_client, Client
from dotenv import load_dotenv
import os
load_dotenv()

router = APIRouter()
supabase: Client = create_client(os.environ.get("SUPABASE_URL"), os.environ.get("SUPABASE_KEY"))
last_data = ""
@router.get("/hit_od")
async def hit_od(data : str):
    last_data = data
    return {"message": "Stock added successfully", "data": ""}

#fetchinggg
@router.get("/read_od")
async def read_od():
    
    return {"data": "last_data"}