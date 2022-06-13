from sqlalchemy import Column, Integer, String, Boolean, Date , ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class Doctor(Base):
    id = Column(Integer,primary_key=True,index=True)
    fullname = Column(String,nullable=False)
    qualif = Column(String, nullable=False) #do
    experience = Column(String, nullable=False)  # do
    shedule = Column(String, nullable=False)  # do
    services = Column(String, nullable=False)  # do
    type = Column(String,nullable=False)   #company
    salary = Column(String)  #company_url
    tod = Column(String,nullable=False) #location
    description = Column(String)
    date_posted = Column(Date)
    is_active = Column(Boolean(),default = True)
    owner_id = Column(Integer,ForeignKey('user.id'))
    owner = relationship("User",back_populates="doctors")