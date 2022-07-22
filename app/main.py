from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.model import SearchItem


app = FastAPI()

@app.get("/distance")
def get_distance(origin: str, destination: str, session: Session = Depends(get_db)):
    obj = {
        "origin": origin,
        "destination": destination,
    }
    session.add(SearchItem(**obj))
    session.commit()
    return obj

@app.get("/history")
def get_history(session: Session = Depends(get_db)):
    return session.query(SearchItem).all()
