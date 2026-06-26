from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from scalar_fastapi import get_scalar_api_reference
from datetime import datetime
from typing import List
from pydantic import BaseModel

from app.database import get_db, engine
from app.models import Mesure, Base

# Crée la table automatiquement si elle n'existe pas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mon API", docs_url=None)

# --- Schéma Pydantic ---
class MesureSchema(BaseModel):
    id: int
    capteur: str
    valeur: float
    horodatage: datetime

    class Config:
        from_attributes = True

# --- Routes ---
@app.get("/")
def racine():
    return {"message": "API operationnelle"}

@app.get("/mesures", response_model=List[MesureSchema])
def get_mesures(db: Session = Depends(get_db)):
    return db.query(Mesure).all()

@app.post("/mesures/seed")
def seed_mesures(db: Session = Depends(get_db)):
    donnees = [
        Mesure(capteur="temperature", valeur=21.5, horodatage=datetime(2024, 1, 1, 8, 0)),
        Mesure(capteur="temperature", valeur=23.1, horodatage=datetime(2024, 1, 1, 9, 0)),
        Mesure(capteur="humidite",    valeur=65.0, horodatage=datetime(2024, 1, 1, 8, 0)),
        Mesure(capteur="humidite",    valeur=63.4, horodatage=datetime(2024, 1, 1, 9, 0)),
        Mesure(capteur="pression",    valeur=1013.2, horodatage=datetime(2024, 1, 1, 8, 0)),
    ]
    db.add_all(donnees)
    db.commit()
    return {"message": f"{len(donnees)} mesures insérées"}

@app.get("/docs", include_in_schema=False)
def scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )