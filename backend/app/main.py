from fastapi import FastAPI
from app.routes import documents, auth

app = FastAPI(title="Smart Document Workflow AI")

app.include_router(auth.router)
app.include_router(documents.router)

@app.get("/")
def read_root():
    return {"message": "API is running"}
