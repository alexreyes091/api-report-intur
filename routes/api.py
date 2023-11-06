from fastapi import APIRouter
from connections.queryActivation import getRequestActivation
from connections.queryChangePrice import getRequestChangePrice
from connections.queryCreation import getRequestCreation
from connections.queryDeactivation import getRequestDeactivation
from connections.queryDocuments import getRequestDocument

router = APIRouter(prefix="/api/reports",
                tags=["Reportes"],
                responses={404: {"description": "Not found"}})

@router.get("/changePrice/{requestId}")
async def api(requestId: int):
    return {
        'request': getRequestChangePrice(requestId),
    }

@router.get("/creation/{requestId}")
async def api(requestId: int):
    return {
        'request': getRequestCreation(requestId),
    }

@router.get("/deactivation/{requestId}")
async def api(requestId: int):
    return {
        'request': getRequestDeactivation(requestId),
    }

@router.get("/document/download/{id}/{requestId}")
async def api(id: int, requestId: int):
    return getRequestDocument(id, requestId)

@router.get("/activation/{requestId}")
async def api(requestId: int):
    return {
        'request': getRequestActivation(requestId),
    }