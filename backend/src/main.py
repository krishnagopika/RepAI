from fastapi import FastAPI
from src.db import base, session
from src.api.v1.routes import company_route
from src.models import company

# Create all tables
base.Base.metadata.create_all(bind=session.engine)

app = FastAPI(title="RepAI Backend")

app.include_router(company_route.router)

@app.get("/")
def root():
    return {"message": "RepAI backend running successfully"}
