from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from scalar_fastapi import get_scalar_api_reference
from datetime import datetime
from typing import List
from pydantic import BaseModel

from app.database import get_db, engine
from app.models import Mesure, Bets, Base

Base.metadata.create_all(bind=engine)


app = FastAPI(title="Mon API", docs_url=None)
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Schémas Pydantic ---
class MesureSchema(BaseModel):
    id: int
    capteur: str
    valeur: float
    horodatage: datetime

    class Config:
        from_attributes = True

class ProchainMatchSchema(BaseModel):
    id: int
    equipe_domicile: str
    equipe_exterieure: str
    date: datetime
    stage: str

class ClassementSchema(BaseModel):
    equipe: str
    joues: int
    victoires: int
    nuls: int
    defaites: int
    points: int


class BetsSchema(BaseModel):
    id: int
    pseudo: str
    match_id: int
    choix: str
    mise: float
    statut: str

class BetCreate(BaseModel):
    pseudo: str
    match_id: int
    choix: str
    mise: float

# --- Routes ---
@app.get("/")
def racine():
    return {"message": "API operationnelle"}


@app.get("/bets", response_model=List[BetsSchema])
def get_bets(db: Session = Depends(get_db)):
    return db.query(Bets).all()


@app.post("/bets", response_model=BetsSchema)
def create_bet(bet: BetCreate, db: Session = Depends(get_db)):
    db_bet = Bets(
        pseudo=bet.pseudo,
        match_id=bet.match_id,
        choix=bet.choix,
        mise=bet.mise,
        statut="En cours"
    )
    db.add(db_bet)
    db.commit()
    db.refresh(db_bet)
    return db_bet

@app.post("/bets/settle")
def settle_bets(db: Session = Depends(get_db)):

    bets = db.query(Bets).filter(Bets.statut == "En cours").all()

    for bet in bets:
        result = db.execute(
             text("SELECT gagnant FROM coupe_du_monde.matchs_termines WHERE id = :match_id").params(match_id=bet.match_id)
        ).fetchone()

        if result is None:
            continue
        if bet.choix == result.gagnant:
            bet.statut = "Gagné"
        else:
            bet.statut = "Perdu"
        
    db.commit()
    return {"message": f"Les paris ont été réglés. {len(bets)} paris mis à jour."}




@app.get('/prochains_matchs', response_model=List[ProchainMatchSchema])
def get_prochains_matchs(db: Session = Depends(get_db)):
    result = db.execute(
        text("SELECT id, equipe_domicile, equipe_exterieure, date, stage FROM coupe_du_monde.prochains_matchs")
    ).fetchall()
    return [dict(row._mapping) for row in result]


@app.get("/classement", response_model=List[ClassementSchema])
def get_classement(db: Session = Depends(get_db)):
    result = db.execute(
        text("SELECT equipe, joues, victoires, nuls, defaites, points FROM coupe_du_monde.classement_cdm")
    ).fetchall()
    return [dict(row._mapping) for row in result]

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