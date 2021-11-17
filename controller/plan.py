from fastapi import APIRouter, Depends
from fastapi.security import APIKeyHeader

from model.plan import CreatePlan, UpdatePlan, DeletePlan
from module.plan import create_plan, read_plan, delete_plan
from module.token_func import user_id_get

router = APIRouter()

api_key = APIKeyHeader(name="Authorization", auto_error=False)


@router.post("/plan", tags=["plan"])
async def create_plan_controller(plan: CreatePlan,
                                 authorization: str = Depends(api_key)):
    user_id = user_id_get(authorization.split()[1])
    create_plan(plan, user_id)

    return plan


@router.put("/plan", tags=["plan"])
async def update_plan_controller(plan: UpdatePlan,
                                 authorization: str = Depends(api_key)):
    user_id = user_id_get(authorization.split()[1])

    return plan


@router.get("/plan", tags=["plan"])
async def read_plan_controller(authorization: str = Depends(api_key)):
    user_id = user_id_get(authorization.split()[1])
    response_list = read_plan(user_id)

    return {"results": response_list}


@router.delete("/plan", tags=["plan"])
async def delete_plan_controller(plan: DeletePlan,
                                 authorization: str = Depends(api_key)):
    user_id = user_id_get(authorization.split()[1])
    delete_plan(plan, user_id)

    return plan
