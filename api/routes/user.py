from fastapi import APIRouter, HTTPException

from db.repositories.user_repository import UserRepository
from models.user.models import UserCreate, UserUpdate

router = APIRouter()


@router.post("/")
async def create(request: UserCreate):
    user_id = UserRepository.create(request)
    if user_id == UserRepository.Exists:
        raise HTTPException(status_code=400, detail="User Already Exists")
    return user_id


@router.get("/{id}")
async def get(id):
    user = UserRepository.get_by_id(id)
    if not user:
        raise HTTPException(status_code=404, detail="Item not found")
    return user


@router.put("/{id}", status_code=200)
async def update(id, req: UserUpdate):
    updated = UserRepository.update(id, req)
    if not updated:
        raise HTTPException(status_code=404, detail="Item not found")
    return ""


@router.delete("/{id}", status_code=200)
async def delete(id):
    if not UserRepository.delete(id):
        raise HTTPException(status_code=404, detail="Item not found")
    return ""
