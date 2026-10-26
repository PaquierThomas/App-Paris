# commande principale local 8000

docker compose up -d
docker compose ps

vérifie svp

cd backend
source .venv/Scripts/activate
uvicorn app.main:app --reload


## puis faire

cd frontend
npm run i
npm run dev

