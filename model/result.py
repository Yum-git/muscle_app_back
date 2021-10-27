from pydantic import BaseModel


class CreateResult(BaseModel):
    result_name: str
    result_count: int
    result_time: str


class UpdateResult(BaseModel):
    id_: int
    result_name: str
    result_count: int
    result_time: str


class ReadResult(BaseModel):
    result_name: str


class DeleteResult(BaseModel):
    id_: int
