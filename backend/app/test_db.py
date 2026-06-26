from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://tsadmin:strongpassword123@localhost:5433/tsdb"
)

with engine.connect() as conn:
    print("Connexion OK")