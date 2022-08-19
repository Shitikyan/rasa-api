from fastapi import APIRouter, HTTPException

from db.repositories.chat_repository import ChatRepository
from models.chat.models import ChatCreate, ChatUpdate

router = APIRouter()


@router.post("/")
async def create(request: ChatCreate):
    chat_id = ChatRepository.create(request)
    if chat_id == ChatRepository.Exists:
        raise HTTPException(status_code=400, detail="Chat Already Exists")
    return chat_id


@router.get("/{id}")
async def get(id):
    chat = ChatRepository.get_by_id(id)
    if not chat:
        raise HTTPException(status_code=404, detail="Item not found")
    return chat


@router.put("/{id}", status_code=200)
async def update(id, req: ChatUpdate):
    updated = ChatRepository.update(id, req)
    if not updated:
        raise HTTPException(status_code=404, detail="Item not found")
    return ""


@router.delete("/{id}", status_code=200)
async def delete(id):
    if not ChatRepository.delete(id):
        raise HTTPException(status_code=404, detail="Item not found")
    return ""
