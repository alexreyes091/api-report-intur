from fastapi import FastAPI
from routes import api
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(api.router)

origins = [
    "http://localhost:8085",
    "https://localhost:8085",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
