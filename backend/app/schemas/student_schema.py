from pydantic import BaseModel

class StudentLogin(BaseModel):
    roll_no: str
    password: str
