from typing import List
from typing import Optional

from fastapi import Request


class DoctorCreateForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.fullname: Optional[str] = None
        self.qualif: Optional[str] = None
        self.experience: Optional[str] = None
        self.shedule: Optional[str] = None
        self.services: Optional[str] = None
        self.type: Optional[str] = None
        self.salary: Optional[str] = None
        self.tod: Optional[str] = None
        self.description: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.fullname = form.get("fullname")
        self.qualif = form.get("qualif")
        self.experience = form.get("experience")
        self.shedule = form.get("shedule")
        self.services = form.get("services")
        self.type = form.get("type")
        self.salary = form.get("salary")
        self.tod = form.get("tod")
        self.description = form.get("description")

    def is_valid(self):
        if not self.description or not len(self.description) >= 20:
            self.errors.append("Description too short")
        if not self.errors:
            return True
        return False
