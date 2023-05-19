from fastapi import APIRouter
from connections.queryChangePrice import getRequest, getUserSignature

router = APIRouter(prefix="/reports",
                tags=["Reportes"],
                responses={404: {"description": "Not found"}})

@router.get("/changePrice/{request_id}")
async def report(request_id: int):
    return {
        'request': getRequest(request_id),
    }

@router.get("/changePrice/userSignature/{user_id}")
async def report(user_id: int):
    return {
        'userSignature': getUserSignature(user_id),
    }