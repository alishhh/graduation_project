from sqlalchemy.orm import Session 

from schemas.doctors import DoctorCreate
from db.models.doctors import Doctor


def create_new_doctor(doctor: DoctorCreate,db : Session,owner_id:int):
    doctor = Doctor(**doctor.dict(),owner_id = owner_id)
    db.add(doctor)
    db.commit()
    db.refresh(doctor)
    return doctor


def retreive_doctor(id:int,db:Session):
    doctor = db.query(Doctor).filter(Doctor.id==id).first()
    return doctor


def list_doctors(db: Session):
    doctors = db.query(Doctor).filter(Doctor.is_active==True).all()
    return doctors


def update_doctor_by_id(id:int,doctor:DoctorCreate,db:Session,owner_id:int):
    existing_doctor = db.query(Doctor).filter(Doctor.id == id)
    if not existing_doctor.first():
        return 0
    doctor.__dict__.update(owner_id=owner_id)
    existing_doctor.update(doctor.__dict__)
    db.commit()
    return 1


def delete_doctor_by_id(id:int,db:Session,owner_id):
    existing_doctor = db.query(Doctor).filter(Doctor.id ==id)
    if not existing_doctor.first():
        return 0
    existing_doctor.delete(synchronize_session=False)
    db.commit()
    return 1