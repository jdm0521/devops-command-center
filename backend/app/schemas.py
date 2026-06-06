from pydantic import BaseModel
from datetime import datetime
#API Layer

class IncidentCreate(BaseModel):
    title: str
    severity: str
    status: str


class IncidentResponse(IncidentCreate):
    id: int

    class Config:
        from_attributes = True
        

class IncidentStatusUpdate(BaseModel):
    status: str
    
class ChangeRequestCreate(BaseModel):
    title: str
    description: str
    requested_by: str
    status: str
    scheduled_time: datetime

class ChangeRequestResponse(ChangeRequestCreate):
    id: int

    class Config:
        from_attributes = True