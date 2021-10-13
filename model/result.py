from pydantic import BaseModel


class Result(BaseModel):
    id_: int = None
    result_name: str = None
    result_count: int = None
    result_time: str = None
