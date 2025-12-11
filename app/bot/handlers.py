from aiogram import Router, types, F
from aiogram.filters import CommandStart
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.user import User

router = Router()


def get_db() -> Session:
    return SessionLocal()


@router.message(CommandStart())
async def start(message: types.Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Отправить номер", request_contact=True)]
        ],
        resize_keyboard=True,
    )
    await message.answer("Отправьте номер телефона:", reply_markup=kb)


@router.message(F.contact)
async def contact_handler(message: types.Message):
    contact = message.contact
    db = get_db()

    try:
        user = (
            db.query(User)
            .filter(User.telegram_id == message.from_user.id)
            .first()
        )

        if not user:
            user = User(
                telegram_id=message.from_user.id,
                phone=contact.phone_number,
                first_name=message.from_user.first_name,
                last_name=message.from_user.last_name,
                username=message.from_user.username,
            )
            db.add(user)
            db.commit()

        await message.answer("Номер сохранён! Спасибо.", reply_markup=None)

    finally:
        db.close()
