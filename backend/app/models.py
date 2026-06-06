from sqlalchemy import Column, Integer, String, DateTime

from app.database import Base

#Database Table
class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String)

    severity = Column(String)

    status = Column(String)
    
class ChangeRequest(Base):
    __tablename__ = "change_requests"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String)

    description = Column(String)

    requested_by = Column(String)

    status = Column(String)

    scheduled_time = Column(DateTime)