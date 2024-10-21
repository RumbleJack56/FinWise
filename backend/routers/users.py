from fastapi import APIRouter
from datetime import date
from supabase import create_client, Client
from dotenv import load_dotenv
import os
load_dotenv()

router = APIRouter()
supabase: Client = create_client(os.environ.get("SUPABASE_URL"), os.environ.get("SUPABASE_KEY"))


@router.get("/")
async def rootfunction():
    return {"message": "UserRoot"}

# TODO:
# make function with parameters , insert to supabase , search in supabase using email , and get uuid, return uuid in json.
@router.get("/add")
async def add_user(name :str , email : str , dob : str, broker: str , password : str):
    # "02/12/2023"  -----(split('/'))---->  [ "02" , "12" , "2023" ] ----([::-1])---->  ["2023" , "12" , "02"]  
    # ----(date())----> converts to date object to send to supabase
    response = supabase.table('users').insert({
        'name' : name,
        'email': email,
        'dob': date(list(map(lambda x:int(x) , *(dob.split('/')[::-1])))),
        'broker': broker,
        'password': password
    }).execute()
    
    print(response)
    return response
