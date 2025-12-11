from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_partner
from app.models.user import User
from app.models.message import Message
from app.schemas.partner import (
    CheckPhoneResponse,
    SendMessageRequest,
    SendMessageResponse,
)
from app.bot.sender import send_message_to_user

router = APIRouter(prefix="/partner", tags=["Partners"])


@router.get("/check-phone", response_model=CheckPhoneResponse)
async def check_phone(
    phone: str,
    db: Session = Depends(get_db),
):
    user = db.query(User).filter(User.phone == phone).first()
    return CheckPhoneResponse(exists=bool(user))


@router.post("/send-message", response_model=SendMessageResponse)
async def send_message(
    payload: SendMessageRequest,
    db: Session = Depends(get_db),
    partner=Depends(get_partner),
):
    user = db.query(User).filter(User.phone == payload.phone).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    msg = Message(
        partner_id=partner.id,
        user_id=user.id,
        phone=payload.phone,
        message=payload.message,
    )
    db.add(msg)
    db.commit()

    await send_message_to_user(user.telegram_id, payload.message)

    return SendMessageResponse(status="sent")
