from typing import Optional
from pydantic import BaseModel
from datetime import date,datetime


class DoctorBase(BaseModel):
    fullname : Optional[str] = None
    spec : Optional[str] =None 
    salary : Optional[str] = None
    tod : Optional[str] = "Remote"
    description : Optional[str] = None
    date_posted : Optional[date] = datetime.now().date()


class DoctorCreate(DoctorBase):
    fullname : str
    spec : str 
    tod : str 
    description : str 


class ShowDoctor(DoctorBase):
    fullname :str
    spec: str 
    salary : Optional[str]
    tod : str 
    date_posted : date 
    description : Optional[str]

    class Config():
        orm_mode = True

    
