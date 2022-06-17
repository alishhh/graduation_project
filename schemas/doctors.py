from typing import Optional
from pydantic import BaseModel
from datetime import date,datetime


class DoctorBase(BaseModel):
    fullname : Optional[str] = None
    qualif : Optional[str] = None
    experience: Optional[str] = None
    shedule: Optional[str] = None
    services: Optional[str] = None
    type : Optional[str] = None
    salary : Optional[str] = None
    tod : Optional[str] = "Terapevt"
    description : Optional[str] = None
    date_posted : Optional[date] = datetime.now().date()


class DoctorCreate(DoctorBase):
    fullname : str
    qualif : str
    experience: str
    shedule: str
    services: str
    type : str
    tod : str
    description : str 


class ShowDoctor(DoctorBase):
    fullname : str
    qualif : str
    experience: str
    shedule: str
    services: str
    type: str
    salary : Optional[str]
    tod : str
    date_posted : date 
    description : Optional[str]

    class Config():
        orm_mode = True

    
