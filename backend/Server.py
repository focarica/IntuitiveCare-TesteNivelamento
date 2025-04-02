from dotenv import load_dotenv
import os

from fastapi import FastAPI, HTTPException, Query
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


load_dotenv()
engine = create_engine(os.getenv('DB_CONNECTION'))


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
app = FastAPI()

