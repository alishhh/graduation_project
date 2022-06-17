from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi import Request,HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session

from db.session import get_db
from webapps.auth.forms import LoginForm
from apis.version1.route_login import login_for_access_token

templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)

@router.get("/login/")
def login(request : Request):
    return templates.TemplateResponse("auth/login.html",{"request":request})


@router.post("/login/")
async def login(request : Request,db : Session = Depends(get_db)):
    form = LoginForm(request)
    await form.load_data() 
    if await form.is_valid():
        try:
            form.__dict__.update(msg="Login Successful :)")
            response = templates.TemplateResponse("auth/login.html", form.__dict__)
            login_for_access_token(response=response,form_data=form,db=db)
            #return response
            return templates.TemplateResponse("other/homepagevs.html", {"request": request})

        except HTTPException:
            form.__dict__.update(msg="")
            form.__dict__.get("errors").append("Incorrect email or password")
            return templates.TemplateResponse("auth/login.html",form.__dict__)
    return templates.TemplateResponse("auth/login.html",form.__dict__)


@router.get("/homevs/")
def homevs(request : Request):
    return templates.TemplateResponse("other/homepagevs.html",{"request":request})


@router.get("/medcenters/")
def medcenters(request : Request):
    return templates.TemplateResponse("other/medcenters.html",{"request":request})



@router.get("/rec/")
def rec(request : Request):
    return templates.TemplateResponse("other/rec.html",{"request":request})


@router.get("/de/")
def de(request : Request):
    return templates.TemplateResponse("other/doctorexmpl.html",{"request":request})