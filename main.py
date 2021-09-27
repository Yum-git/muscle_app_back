from typing import List

from fastapi import FastAPI, Response
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


class Count(BaseModel):
    argument: str
    value: int


class Counts(BaseModel):
    results: List[Count]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/counts")
async def read_count(PoseName: str, response: Response):
    """
    過去のカウント数を取得する関数
    Query
    type_key: 運動タイプ
    month_key: 月

    Header
    Bearer Token: GoogleJWTToken
    """
    if PoseName == 'Squat':
        response_data = {
            "results": [
                {"argument": "01-03", "value": 20},
                {"argument": "01-04", "value": 10},
                {"argument": "01-05", "value": 0},
                {"argument": "01-06", "value": 10},
                {"argument": "01-07", "value": 30},
                {"argument": "01-08", "value": 0},
                {"argument": "01-09", "value": 10},
                {"argument": "01-10", "value": 30}
            ],
            "status": 200
        }
    elif PoseName == 'PushUp':
        response_data = {
            "results": [
                {"argument": "01-03", "value": 30},
                {"argument": "01-04", "value": 40},
                {"argument": "01-05", "value": 10},
                {"argument": "01-06", "value": 0},
                {"argument": "01-07", "value": 0},
                {"argument": "01-08", "value": 20},
                {"argument": "01-09", "value": 30},
                {"argument": "01-10", "value": 0}
            ],
            "status": 200
        }
    else:
        response_data = {
            "status": 404
        }
        response.status_code = 404

    return response_data
