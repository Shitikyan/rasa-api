from fastapi import APIRouter, HTTPException

from db.repositories.login_repository import LoginRepository
from models.login.models import LoginCreate, LoginUpdate

router = APIRouter()


@router.post("/")
async def create(request: LoginCreate):
    login_id = LoginRepository.create(request)
    if login_id == LoginRepository.Exists:
        raise HTTPException(status_code=400, detail="Login Already Exists")
    return login_id


@router.get("/{id}")
async def get(id):
    login = LoginRepository.get_by_id(id)
    if not login:
        raise HTTPException(status_code=404, detail="Item not found")
    return login


@router.put("/{id}", status_code=200)
async def update(id, req: LoginUpdate):
    updated = LoginRepository.update(id, req)
    if not updated:
        raise HTTPException(status_code=404, detail="Item not found")
    return ""


@router.delete("/{id}", status_code=200)
async def delete(id):
    if not LoginRepository.delete(id):
        raise HTTPException(status_code=404, detail="Item not found")
    return ""
