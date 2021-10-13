from pydantic import BaseModel, EmailStr


class UserValidator(BaseModel):
    """Используем для разнообразия не json-схему, а pydantic."""
    email: EmailStr
    password_hash: str
