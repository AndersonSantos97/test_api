from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
from .conexion import SessionLocal, engine
from . import models, schemas
from typing import List

app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")

@app.get("/nationalities", response_model=List[schemas.Nationalities])
def list_nationalities(db:Session = Depends(get_db)):
    nationalities = db.query(models.Nationalities).all()
    return nationalities