from pydantic import BaseModel, ConfigDict
from datetime import datetime


class UserResponse(BaseModel):
    id: int
    github_id: str
    username: str
    email: str | None = None
    avatar_url: str | None = None
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)