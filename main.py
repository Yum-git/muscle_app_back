from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/counts")
async def read_count(type_key: str):
    if type_key == 'squat':
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
    elif type_key == 'pushup':
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

    return response_data
