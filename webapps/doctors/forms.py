from typing import List
from typing import Optional

from fastapi import Request


class DoctorCreateForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.fullname: Optional[str] = None
        self.company: Optional[str] = None
        self.company_url: Optional[str] = None
        self.location: Optional[str] = None
        self.description: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.fullname = form.get("fullname")
        self.company = form.get("company")
        self.company_url = form.get("company_url")
        self.location = form.get("location")
        self.description = form.get("description")

    def is_valid(self):
        if not self.description or not len(self.description) >= 20:
            self.errors.append("Description too short")
        if not self.errors:
            return True
        return False
