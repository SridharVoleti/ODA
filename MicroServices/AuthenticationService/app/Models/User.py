from pydantic import BaseModel,Field
from fastapi.encoders import jsonable_encoder
from typing import Optional
from enum import Enum
from datetime import datetime

class User(BaseModel):
    userId:str=Field(None, alias="_id")
    firstname:str
    middlename:Optional[str]=None
    lastname:str
    address:str
    phone:str
    username:str
    password:str
    role:str
    CreatedAt:datetime
    UpdatedAt:Optional[datetime]=None

    def to_json(self):
        return jsonable_encoder(self,exclude_none=True)
    
    def to_bson(self):
        return self.model_dump(exclude_none=True)
