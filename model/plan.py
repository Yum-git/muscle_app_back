from typing import Optional

from pydantic import BaseModel


class CreatePlan(BaseModel):
    plan_name: str
    start_time: str
    end_time: str
    plan_notes: Optional[str] = None


class UpdatePlan(BaseModel):
    id_: int
    plan_name: Optional[str] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    plan_notes: Optional[str] = None


class ReadPlan(BaseModel):
    id_: int


class DeletePlan(BaseModel):
    id_: int
