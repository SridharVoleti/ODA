from pydantic import BaseModel,Field
from fastapi.encoders import jsonable_encoder
from datetime import datetime,timedelta

class Invitation(BaseModel):
    invite_id:str=Field(None, alias="_id")
    email:str
    role:str
    expiry:datetime = datetime.now()+timedelta(days=7)
    is_used:bool = False

    def to_json(self):
        return jsonable_encoder(self,exclude_none=True,by_alias=True)
    
    def to_bson(self):
        return self.model_dump(exclude_none=True,by_alias=True)
