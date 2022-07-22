from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from app.db import get_db
from app.geography import calculate_distance
from app.model import SearchItem
from app.nominatim import search_nominatim


app = FastAPI()

app.mount("/web", StaticFiles(directory="app/static"), name="static")

@app.get("/distance")
def get_distance(origin: str, destination: str, session: Session = Depends(get_db)):
    
    origin_results = search_nominatim(origin)
    destination_results = search_nominatim(destination)

    origin_guess = origin_results[0]
    destination_guess = destination_results[0]

    distance = calculate_distance(
        *(float(angle) for angle in
          (origin_guess['lat'], origin_guess['lon'], destination_guess['lat'], destination_guess['lon'])
        )
    )
    
    obj = {
        "origin": origin,
        "destination": destination,
        'distance': distance
    }
    session.add(SearchItem(**obj))
    session.commit()

    return obj

@app.get("/history")
def get_history(session: Session = Depends(get_db)):
    return session.query(SearchItem).all()
