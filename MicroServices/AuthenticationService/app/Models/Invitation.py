from pydantic import BaseModel, Field
from fastapi.encoders import jsonable_encoder
from datetime import datetime, timedelta
from typing import Optional

class Invitation(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")  
    email: str
    role: str
    expiry: datetime = Field(default_factory=lambda: datetime.now() + timedelta(days=7))
    is_used: Optional[bool] = False

    def to_json(self):
        return jsonable_encoder(self, exclude_none=True)
    
    def to_bson(self):
        data = self.model_dump(by_alias=True, exclude_none=True)
        return data
