from fastapi import Depends, APIRouter
from fastapi.security import APIKeyHeader

# model
from model.result import CreateResult, UpdateResult, DeleteResult

# module
from module.result import create_result, update_result, read_result, delete_result
from module.token_func import user_id_get

router = APIRouter()

api_key = APIKeyHeader(name="Authorization", auto_error=False)


@router.post("/result", tags=["result"])
async def create_result_controller(result: CreateResult,
                                   authorization: str = Depends(api_key)):
    user_id = user_id_get(authorization.split()[1])
    create_result(result,
                  user_id)

    return result


@router.put("/result", tags=["result"])
async def update_result_controller(result: UpdateResult,
                                   authorization: str = Depends(api_key)):
    user_id = user_id_get(authorization.split()[1])
    update_result(result,
                  user_id)

    return result


@router.get("/result", tags=["result"])
async def read_result_controller(pose: str, authorization: str = Depends(api_key)):
    user_id = user_id_get(authorization.split()[1])

    response_list = read_result(pose, user_id)

    return {"results": response_list}


@router.delete("/result", tags=["result"])
async def delete_result_controller(result: DeleteResult,
                                   authorization: str = Depends(api_key)):
    user_id = user_id_get(authorization.split()[1])
    delete_result(result,
                  user_id)

    return result
