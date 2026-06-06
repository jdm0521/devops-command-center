from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine, get_db
from app.models import Base, Incident, ChangeRequest
from app.schemas import (
    IncidentCreate,
    IncidentStatusUpdate,
    IncidentResponse,
    ChangeRequestCreate,
    ChangeRequestResponse
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "DevOps Command Center API"}


@app.post("/incidents")
def create_incident(
    incident: IncidentCreate,
    db: Session = Depends(get_db)
):
    new_incident = Incident(
        title=incident.title,
        severity=incident.severity,
        status=incident.status
    )

    db.add(new_incident)

    db.commit()

    db.refresh(new_incident)

    return new_incident


@app.get("/incidents", response_model=list[IncidentResponse])
def get_incidents(
    db: Session = Depends(get_db)
):
    incidents = db.query(Incident).all()

    return incidents


@app.get("/incidents/{incident_id}", response_model=IncidentResponse)
def get_incident(
    incident_id: int,
    db: Session = Depends(get_db)
):
    incident = (
        db.query(Incident)
        .filter(Incident.id == incident_id)
        .first()
    )
    
    if incident is None:
        raise HTTPException(
        status_code=404,
        detail="Incident not found"
        )

    return incident

@app.put("/incidents/{incident_id}")
def update_incident_status(
    incident_id: int,
    update: IncidentStatusUpdate,  #converts it into a Pydantic object.
    db: Session = Depends(get_db)
):
    incident = (
        db.query(Incident)
        .filter(Incident.id == incident_id)
        .first()
    )

    if incident is None:
        raise HTTPException(
        status_code=404,
        detail="Incident not found"
        )

    incident.status = update.status

    db.commit()

    db.refresh(incident)

    return incident


@app.delete("/incidents/{incident_id}")
def delete_incident(
    incident_id: int,
    db: Session = Depends(get_db)
):
    incident = (
        db.query(Incident)
        .filter(Incident.id == incident_id)
        .first()
    )

    if incident is None:
        raise HTTPException(
        status_code=404,
        detail="Incident not found"
        )

    db.delete(incident)

    db.commit()

    return {"message": "Incident deleted successfully"}

@app.post(
    "/change-requests",
    response_model=ChangeRequestResponse
)
def create_change_request(
    change_request: ChangeRequestCreate,
    db: Session = Depends(get_db)
):
    new_change_request = ChangeRequest(
        title=change_request.title,
        description=change_request.description,
        requested_by=change_request.requested_by,
        status=change_request.status,
        scheduled_time=change_request.scheduled_time
    )

    db.add(new_change_request)

    db.commit()

    db.refresh(new_change_request)

    return new_change_request

@app.get(
    "/change-requests",
    response_model=list[ChangeRequestResponse]
)
def get_change_requests(
    db: Session = Depends(get_db)
):
    change_requests = (
        db.query(ChangeRequest)
        .all()
    )

    return change_requests

@app.get("/change-requests/{change_request_id}")
def get_incident(
    change_request_id: int,
    db: Session = Depends(get_db)
):
    change = (
        db.query(ChangeRequest)
        .filter(ChangeRequest.id == change_request_id)
        .first()
    )
    
    if change is None:
        raise HTTPException(
        status_code=404,
        detail="Change request not found"
        )

    return change