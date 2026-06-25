from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:password123@localhost:5432/postgres"
)

with engine.connect() as conn:
    print("Connexion OK")