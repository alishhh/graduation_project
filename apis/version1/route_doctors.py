from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session

from db.session import get_db
from db.models.doctors import Doctor
from schemas.doctors import DoctorCreate,ShowDoctor
from db.repository.doctors import (create_new_doctor,
        retreive_doctor,list_doctors,
        update_doctor_by_id,
        delete_doctor_by_id)
from apis.version1.route_login import get_current_user_from_token
from db.models.users import User
from typing import List

router = APIRouter()


@router.post("/create-doctor",response_model=ShowDoctor)
def create_doctor(doctor : DoctorCreate,db : Session = Depends(get_db),current_user: User=Depends(get_current_user_from_token)):
    owner_id = current_user.id
    doctor = create_new_doctor(doctor=doctor, db=db, owner_id=owner_id)
    return doctor


@router.get("/get/{id}",response_model=ShowDoctor)
def retreive_doctor_by_id(id:int,db:Session = Depends(get_db)):
    doctor = retreive_doctor(id=id, db=db)
    print(doctor)
    if not doctor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Doctor with id {id} does not exist")
    return doctor


@router.get("/all",response_model=List[ShowDoctor])
def retreive_all_doctors(db:Session = Depends(get_db)):
    doctors = list_doctors(db=db)
    return doctors


@router.put("/update/{id}")
def update_doctor(id:int,doctor:DoctorCreate,db:Session=Depends(get_db),current_user: User=Depends(get_current_user_from_token)):
    owner_id = current_user.id
    doctor_retrieved = retreive_doctor(id=id, db=db)
    if not doctor_retrieved:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Doctor with id {id} does not exist")
    if doctor_retrieved.owner_id == current_user.id or current_user.is_superuser:
        message = update_doctor_by_id(id=id, doctor=doctor, db=db, owner_id=owner_id)
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"You are not authorized to update.")
    return {"detail":"Successfully updated data."}


@router.delete("/delete/{id}")
def delete_doctor(id:int,db:Session=Depends(get_db),current_user:User=Depends(get_current_user_from_token)):
    doctor = retreive_doctor(id=id, db=db)
    if not doctor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Doctor with id {id} does not exist")
    if doctor.owner_id == current_user.id or current_user.is_superuser:
        delete_doctor_by_id(id=id, db=db, owner_id=current_user.id)
        return {"detail":"Doctor Successfully deleted"}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
    detail="You are not permitted!!")