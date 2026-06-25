from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

app = FastAPI(title="Mon API", docs_url=None)

@app.get("/")
def racine():
    return {"message": "API operationnelle"}

@app.get("/docs", include_in_schema=False)
def scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )