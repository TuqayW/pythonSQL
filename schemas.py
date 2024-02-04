from pydantic import BaseModel

class StudentCreate(BaseModel):
    name:str
    surname:str
    age:int 
    score:float

class Student(BaseModel):
    id:int
    name:str
    surname:str
    age:int 
    score:float

    class Config:
        from_attributes=True


class TeacherCreate(BaseModel):
    name:str
    surname:str
    subject:str
    age:int
    experience:float

class Teacher(BaseModel):
    id:int
    name:str
    surname:str
    subject:str
    age:int
    experience:float

    class Config:
        from_attributes=True