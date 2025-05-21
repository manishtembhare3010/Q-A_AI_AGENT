from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Knowledge Agent API")

app.include_router(router)