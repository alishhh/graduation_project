from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import responses, status
from fastapi.security.utils import get_authorization_scheme_param
from db.repository.doctors import list_doctors
from sqlalchemy.orm import Session
from db.session import get_db
from fastapi import Depends
from db.repository.doctors import retreive_doctor

from db.models.users import User  
from apis.version1.route_login import get_current_user_from_token
from webapps.doctors.forms import DoctorCreateForm
from schemas.doctors import DoctorCreate
from db.repository.doctors import create_new_doctor


templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/")
def home(request:Request,db:Session = Depends(get_db),msg:str = None):
    doctors = list_doctors(db=db)
    return templates.TemplateResponse("doctors/homepage.html",{"request":request,"doctors":doctors,"msg":msg})


@router.get("/detail/{id}")
def doctor_detail(id:int, request:Request,db:Session = Depends(get_db)):
    doctor = retreive_doctor(id=id, db=db)
    return templates.TemplateResponse("doctors/detail.html", {"request":request,
    "doctor":doctor})


@router.get("/post-a-doctor/")
def create_doctor(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("doctors/create_doctor.html", {"request": request})


@router.post("/post-a-doctor/")
async def create_doctor(request: Request, db: Session = Depends(get_db)):
    form = DoctorCreateForm(request)
    await form.load_data()
    if form.is_valid():
        try:
            token = request.cookies.get("access_token")
            scheme, param = get_authorization_scheme_param(
                token
            )  # scheme will hold "Bearer" and param will hold actual token value
            current_user: User = get_current_user_from_token(token=param, db=db)
            doctor = DoctorCreate(**form.__dict__)
            doctor = create_new_doctor(doctor=doctor, db=db, owner_id=current_user.id)
            return responses.RedirectResponse(
                f"/detail/{doctor.id}", status_code=status.HTTP_302_FOUND
            )
        except Exception as e:
            print(e)
            form.__dict__.get("errors").append(
                "You might not be logged in, In case problem persists please contact us."
            )
            return templates.TemplateResponse("doctors/create_doctor.html", form.__dict__)
    return templates.TemplateResponse("doctors/create_doctor.html", form.__dict__)


@router.get("/delete-doctor/")
def show_doctors_to_delete(request: Request,db : Session = Depends(get_db)):
    doctors = list_doctors(db=db)
    return templates.TemplateResponse("doctors/show_doctors_to_delete.html", {
        "request":request,
        "doctors":doctors
    })
