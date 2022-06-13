from typing import Optional
from pydantic import BaseModel
from datetime import date,datetime


class DoctorBase(BaseModel):
    fullname : Optional[str] = None
    qualif : Optional[str] = None #do
    experience: Optional[str] = None  # do
    shedule: Optional[str] = None  # do services
    services: Optional[str] = None  # do services
    type : Optional[str] = None #company
    salary : Optional[str] = None #company_url
    tod : Optional[str] = "Terapevt" #location
    description : Optional[str] = None
    date_posted : Optional[date] = datetime.now().date()


class DoctorCreate(DoctorBase):
    fullname : str
    qualif : str #do
    experience: str  # do
    shedule: str  # do
    services: str  # do
    type : str #company
    tod : str #location
    description : str 


class ShowDoctor(DoctorBase):
    fullname : str
    qualif : str #do
    experience: str  # do
    shedule: str  # do
    services: str  # do
    type: str
    salary : Optional[str] #company_url
    tod : str #location
    date_posted : date 
    description : Optional[str]

    class Config():
        orm_mode = True

    
