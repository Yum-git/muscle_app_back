import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from controller import result, plan

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000',
                   'http://localhost:5000'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(result.router)
app.include_router(plan.router)
