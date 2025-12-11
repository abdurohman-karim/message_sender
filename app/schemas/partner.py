from pydantic import BaseModel


class CheckPhoneResponse(BaseModel):
    exists: bool


class SendMessageRequest(BaseModel):
    phone: str
    message: str


class SendMessageResponse(BaseModel):
    status: str
