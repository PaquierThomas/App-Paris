from sqlalchemy import Column, Integer, String, Float, DateTime
from .database import Base

class Mesure(Base):
    __tablename__ = "mesures"

    id         = Column(Integer, primary_key=True)
    capteur    = Column(String)
    valeur     = Column(Float)
    horodatage = Column(DateTime)


class Bets(Base):
    __tablename__ = "bets"

    id         = Column(Integer, primary_key=True)
    pseudo     = Column(String)
    match_id   = Column(Integer)
    choix      = Column(String)
    mise       = Column(Float)
    statut     = Column(String) 


    