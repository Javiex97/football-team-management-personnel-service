
from sqlalchemy import create_engine, MetaData
from databases import Database
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = "postgresql://postgres:WbnS5utrc1Gayg35@db.olzrkkjzqltovkvxeggb.supabase.co:5432/postgres"

database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
metadata = MetaData() 